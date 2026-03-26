from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI(title="SDK Target API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Product(BaseModel):
    id: int
    name: str
    price: float
    description: Optional[str] = None

class ProductCreate(BaseModel):
    name: str
    price: float
    description: Optional[str] = None

db = {}

@app.get("/products", response_model=List[Product], tags=["Products"])
def get_products():
    """Retrieve all stored products."""
    return list(db.values())

@app.post("/products", response_model=Product, tags=["Products"])
def create_product(product: ProductCreate):
    """Create a new product."""
    new_id = len(db) + 1
    new_product = Product(id=new_id, **product.model_dump())
    db[new_id] = new_product
    return new_product

@app.get("/products/{product_id}", response_model=Product, tags=["Products"])
def get_product_by_id(product_id: int):
    """Retrieve a product by its ID."""
    if product_id not in db:
        raise HTTPException(status_code=404, detail="Product not found")
    return db[product_id]

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
