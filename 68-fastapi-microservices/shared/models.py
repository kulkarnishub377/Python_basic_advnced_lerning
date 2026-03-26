from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    email: str

class OrderItem(BaseModel):
    product: str
    price: float

class Order(BaseModel):
    order_id: int
    user_id: int
    items: list[OrderItem]
