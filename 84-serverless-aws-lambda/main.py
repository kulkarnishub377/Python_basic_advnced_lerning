from fastapi import FastAPI
from mangum import Mangum

app = FastAPI(title="Serverless FastAPI Event Processor")

@app.get("/")
def read_root():
    return {"message": "Hello from AWS Lambda!"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

# Mangum acts as the adapter for AWS Lambda & API Gateway
handler = Mangum(app)
