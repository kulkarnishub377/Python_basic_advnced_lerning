# 71 - Redis Caching & Invalidation API

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Difficulty: Expert](https://img.shields.io/badge/Difficulty-Expert-red?style=for-the-badge)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Redis](https://img.shields.io/badge/Redis-DC382D?style=for-the-badge&logo=redis&logoColor=white)

## What It Does

Demonstrates advanced **server-side caching** using Redis to dramatically speed up repeated API queries. When a client requests data, the server first checks Redis. If a cached result exists (cache HIT), it returns instantly. If not (cache MISS), it simulates a slow database query, stores the result in Redis with a TTL, and returns it. Write operations (`POST`) automatically invalidate the relevant cache keys.

## Project Structure

```text
71-redis-caching/
  main.py            # FastAPI entry point with cached endpoints
  database.py        # Simulated slow database layer
  redis_client.py    # Redis connection and cache helper functions
  config.py          # Configuration constants (TTL, Redis URL)
  requirements.txt   # Dependencies
  index.html         # Unified frontend dashboard
  README.md          # This file
```

## Setup and Run

### Prerequisites
- Redis server running locally on port 6379 (default)

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Start Redis (if not running)
```bash
redis-server
```

### 3. Start the FastAPI server
```bash
uvicorn main:app --reload
```

### 4. Open the Frontend
Open `index.html` in your browser to test cached vs uncached queries.

## Example Output

```json
// First request (CACHE MISS) - takes ~2 seconds
{
  "source": "database",
  "response_time_ms": 2003,
  "data": [
    {"id": 1, "name": "Laptop", "price": 999.99},
    {"id": 2, "name": "Phone", "price": 699.99}
  ]
}

// Second request (CACHE HIT) - returns instantly
{
  "source": "redis_cache",
  "response_time_ms": 2,
  "data": [
    {"id": 1, "name": "Laptop", "price": 999.99},
    {"id": 2, "name": "Phone", "price": 699.99}
  ]
}
```

## Core Concepts

- **Cache-Aside Pattern**: Application checks cache before querying the database.
- **TTL (Time-To-Live)**: Cached data automatically expires after a configurable duration.
- **Cache Invalidation**: Write operations flush stale cache keys to maintain data consistency.
- **Serialization**: Python dicts are serialized to JSON strings for Redis storage.
