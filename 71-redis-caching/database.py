import time

# Simulated in-memory database
_products = [
    {"id": 1, "name": "Laptop", "price": 999.99},
    {"id": 2, "name": "Phone", "price": 699.99},
    {"id": 3, "name": "Headphones", "price": 149.99},
]


def slow_get_all_products():
    """Simulate a slow database query (2 second delay)."""
    time.sleep(2)
    return _products


def add_product(name: str, price: float):
    """Add a product to the simulated database."""
    new_id = max(p["id"] for p in _products) + 1 if _products else 1
    product = {"id": new_id, "name": name, "price": price}
    _products.append(product)
    return product
