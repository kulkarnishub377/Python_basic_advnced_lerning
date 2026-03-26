# 68 - Microservices with FastAPI

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Difficulty: Advanced](https://img.shields.io/badge/Difficulty-Advanced-orange?style=for-the-badge)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Docker (Conceptual)](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)

## What It Does

Demonstrates a fundamental **Microservices Architecture**. Instead of one monolithic FastAPI app containing all features, we split the application into two entirely separate services:
1. **Users Service** (Port 8001): Manages user data.
2. **Orders Service** (Port 8002): Manages orders. When an order is requested, it uses `httpx` to synchronously communicate over the network with the Users service to fetch the user's details and stitch the data together.

Includes a unified frontend to query the Orders service and see the stitched data.

## Project Structure

```text
68-fastapi-microservices/
  users_service/
    main.py          # Port 8001 server
  orders_service/
    main.py          # Port 8002 server (calls 8001)
  shared/
    models.py        # Pydantic models shared across services (conceptual)
  index.html         # Unified Frontend hitting Port 8002
  requirements.txt   # Dependencies
  README.md          # This file
```

## Setup and Run

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Start Service 1 (Users)

In a new terminal:
```bash
cd users_service
uvicorn main:app --port 8001
```

### 3. Start Service 2 (Orders)

In a new terminal:
```bash
cd orders_service
uvicorn main:app --port 8002
```

### 4. Open the Frontend
Open `index.html` directly in your browser.



## Example Output

```json
{
  "order": {
    "order_id": 101,
    "user_id": 1,
    "items": [{"product": "Laptop", "price": 999.99}]
  },
  "customer": {
    "id": 1,
    "name": "Alice Inwonderland",
    "email": "alice@example.com"
  }
}
```
## Core Concepts

- **Service Separation**: Complete isolation of domains.
- **Service-to-Service Communication**: The Orders service acts as a *client* to the Users service using Python's async `httpx` library.
- **Data Aggregation**: The Orders service stitches together its internal order data with the external user data before returning it to the browser.
