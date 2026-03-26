from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from aggregator import get_metrics

app = FastAPI(title="Kafka Analytics Dashboard API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/metrics")
def metrics():
    """Return the latest aggregated metrics from the Kafka consumer."""
    return get_metrics()


@app.get("/health")
def health():
    return {"status": "ok", "service": "kafka-analytics-api"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("api:app", host="127.0.0.1", port=8000, reload=True)
