"""REST-to-gRPC proxy so browsers can interact with the gRPC server."""
import grpc
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from config import GRPC_SERVER_ADDRESS
import time

try:
    import product_pb2
    import product_pb2_grpc
except ImportError:
    product_pb2 = None
    product_pb2_grpc = None

app = FastAPI(title="gRPC REST Proxy")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class ProductCreate(BaseModel):
    name: str
    price: float


def _get_stub():
    channel = grpc.insecure_channel(GRPC_SERVER_ADDRESS)
    return product_pb2_grpc.ProductServiceStub(channel)


@app.get("/products")
def list_products():
    """Proxy: translate HTTP GET to gRPC ListProducts call."""
    if not product_pb2:
        raise HTTPException(500, "Run python codegen.py first")
    stub = _get_stub()
    resp = stub.ListProducts(product_pb2.Empty())
    return [
        {"id": p.id, "name": p.name, "price": p.price, "in_stock": p.in_stock}
        for p in resp.products
    ]


@app.post("/products")
def create_product(p: ProductCreate):
    """Proxy: translate HTTP POST to gRPC CreateProduct call."""
    if not product_pb2:
        raise HTTPException(500, "Run python codegen.py first")
    stub = _get_stub()
    resp = stub.CreateProduct(
        product_pb2.CreateProductRequest(name=p.name, price=p.price)
    )
    return {"id": resp.id, "name": resp.name, "price": resp.price, "in_stock": resp.in_stock}


@app.get("/benchmark/{n}")
def benchmark(n: int = 100):
    """Run N gRPC calls and return timing data."""
    if not product_pb2:
        raise HTTPException(500, "Run python codegen.py first")
    stub = _get_stub()
    start = time.perf_counter()
    for _ in range(n):
        stub.ListProducts(product_pb2.Empty())
    elapsed = round((time.perf_counter() - start) * 1000, 1)
    return {"calls": n, "total_ms": elapsed, "avg_ms": round(elapsed / n, 2)}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("proxy:app", host="127.0.0.1", port=8000, reload=True)
