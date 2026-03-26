import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import httpx
from shared.models import Order, OrderItem

app = FastAPI(title="Orders Microservice", description="Runs on port 8002 and calls 8001")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

USERS_SERVICE_URL = "http://127.0.0.1:8001"

orders_db = {
    101: Order(order_id=101, user_id=1, items=[OrderItem(product="Laptop", price=999.99)]),
    102: Order(order_id=102, user_id=2, items=[OrderItem(product="Mouse", price=49.99)])
}

@app.get("/orders/{order_id}")
async def get_order_with_user_details(order_id: int):
    """
    Returns an order, but stitches in the user's details by 
    making a network request to the Users Microservice.
    """
    if order_id not in orders_db:
        raise HTTPException(status_code=404, detail="Order not found")
        
    order = orders_db[order_id]
    
    # 1. Start HTTP Client session
    async with httpx.AsyncClient() as client:
        try:
            # 2. Make network call to other microservice
            response = await client.get(f"{USERS_SERVICE_URL}/users/{order.user_id}")
            response.raise_for_status()
            user_data = response.json()
        except httpx.HTTPError:
            # Fallback if users service is offline
            user_data = {"error": "Users microservice is currently unavailable"}
            
    # 3. Stitch data together
    return {
        "order": order,
        "customer": user_data
    }
