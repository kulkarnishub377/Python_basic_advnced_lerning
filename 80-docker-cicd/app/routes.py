from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

# In-memory store
items_db = []


class Item(BaseModel):
    name: str
    price: float
    quantity: int = 1


@router.get("/items")
def get_items():
    """List all items."""
    return {"items": items_db, "count": len(items_db)}


@router.post("/items")
def create_item(item: Item):
    """Create a new item."""
    entry = item.dict()
    entry["id"] = len(items_db) + 1
    items_db.append(entry)
    return {"created": entry}


@router.get("/items/{item_id}")
def get_item(item_id: int):
    """Get a specific item by ID."""
    for item in items_db:
        if item["id"] == item_id:
            return item
    return {"error": "Item not found"}
