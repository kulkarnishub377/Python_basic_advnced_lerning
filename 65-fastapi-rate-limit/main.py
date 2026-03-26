from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from rate_limiter import rate_limit

app = FastAPI(title="Rate Limiting API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/data", dependencies=[Depends(rate_limit)])
async def get_secure_data():
    """
    Protected endpoint. If the user hits this >5 times in 10 seconds,
    the `rate_limit` dependency will raise an HTTP 429 error.
    """
    return {
        "message": "Success! You accessed the protected data.",
        "status": "OK"
    }

@app.get("/api/public")
async def get_public_data():
    """
    Unprotected endpoint. Infinite requests allowed.
    """
    return {
        "message": "Public route. No rate limiting applied here."
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
