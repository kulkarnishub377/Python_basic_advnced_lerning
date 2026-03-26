from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

# --- Legacy Schema ---
class UserV1(BaseModel):
    id: int
    name: str  # v1 uses a single full name string
    email: str

# In a real app, this data would come from a database.
mock_db = [
    UserV1(id=1, name="John Doe", email="john@example.com"),
    UserV1(id=2, name="Jane Smith", email="jane@example.com")
]

@router.get("/users")
async def get_users_v1():
    """Returns users using the legacy v1 schema."""
    return {"version": "v1", "data": mock_db}
