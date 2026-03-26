import time
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from database import slow_get_all_products, add_product
from redis_client import get_cache, set_cache, invalidate_cache, REDIS_AVAILABLE

app = FastAPI(title="Redis Caching API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

CACHE_KEY = "products:all"


class ProductCreate(BaseModel):
    name: str
    price: float


@app.get("/products")
def get_products():
    """
    Returns products. If Redis is available, checks cache first.
    On a cache MISS, fetches from the slow DB and populates cache.
    """
    start = time.perf_counter()

    # 1. Try cache
    cached = get_cache(CACHE_KEY)
    if cached is not None:
        elapsed = round((time.perf_counter() - start) * 1000, 1)
        return {"source": "redis_cache", "response_time_ms": elapsed, "data": cached}

    # 2. Cache miss -- hit the slow database
    data = slow_get_all_products()

    # 3. Populate the cache for next time
    set_cache(CACHE_KEY, data)

    elapsed = round((time.perf_counter() - start) * 1000, 1)
    return {"source": "database", "response_time_ms": elapsed, "data": data}


@app.post("/products")
def create_product(product: ProductCreate):
    """
    Creates a product and invalidates the cache so the next
    GET request fetches fresh data from the database.
    """
    new_product = add_product(product.name, product.price)

    # Invalidate cache so stale data is never served
    deleted_count = invalidate_cache("products:*")

    return {
        "created": new_product,
        "cache_keys_invalidated": deleted_count,
    }


@app.get("/health")
def health():
    return {"redis_available": REDIS_AVAILABLE}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
