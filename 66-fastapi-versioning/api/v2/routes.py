from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

# --- New Schema ---
class UserV2(BaseModel):
    id: int
    first_name: str  # v2 split the name
    last_name: str
    email: str
    is_active: bool  # v2 added a new field

mock_db = [
    UserV2(id=1, first_name="John", last_name="Doe", email="john@example.com", is_active=True),
    UserV2(id=2, first_name="Jane", last_name="Smith", email="jane@example.com", is_active=False)
]

@router.get("/users")
async def get_users_v2():
    """Returns users using the new v2 schema."""
    return {"version": "v2", "data": mock_db}
