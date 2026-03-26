from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

app = FastAPI(
    title="High-Performance Inventory API",
    description="A clean, type-safe RESTful Service",
    version="1.0.0"
)

# In-memory database
inventory = []
current_id = 1

# Pydantic Models intelligently validate data
class ItemCreate(BaseModel):
    name: str
    quantity: int
    price: float
    description: Optional[str] = None

class Item(ItemCreate):
    id: int
    created_at: datetime

@app.post("/items/", response_model=Item, status_code=201)
def create_item(item_in: ItemCreate):
    global current_id
    new_item = Item(
        id=current_id,
        name=item_in.name,
        quantity=item_in.quantity,
        price=item_in.price,
        description=item_in.description,
        created_at=datetime.now()
    )
    inventory.append(new_item)
    current_id += 1
    return new_item

@app.get("/items/", response_model=List[Item])
def get_items():
    return inventory

@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int):
    for item in inventory:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")
