import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from shared.models import User

app = FastAPI(title="Users Microservice", description="Runs on port 8001")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

users_db = {
    1: User(id=1, name="Alice Inwonderland", email="alice@example.com"),
    2: User(id=2, name="Bob Builder", email="bob@example.com"),
}

@app.get("/users/{user_id}", response_model=User)
async def get_user(user_id: int):
    """Returns details for a specific user."""
    if user_id not in users_db:
        raise HTTPException(status_code=404, detail="User not found")
    return users_db[user_id]
