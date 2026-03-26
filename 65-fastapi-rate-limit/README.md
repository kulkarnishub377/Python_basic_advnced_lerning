# 65 - Rate Limiting & Throttling

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Difficulty: Advanced](https://img.shields.io/badge/Difficulty-Advanced-orange?style=for-the-badge)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Redis](https://img.shields.io/badge/Redis-DC382D?style=for-the-badge&logo=redis&logoColor=white)

## What It Does

A custom implementation of a **Sliding Window API Rate Limiter** inside FastAPI using Redis. It protects the `/api/data` endpoint by limiting requests to **5 per 10 seconds** per IP address. If a user exceeds the limit, they are blocked with a `429 Too Many Requests` response. Includes a simple, unified frontend to test spamming the API.

## Project Structure

```text
65-fastapi-rate-limit/
  main.py            # FastAPI Entry point
  rate_limiter.py    # Redis sliding window logic implemented as a Dependency
  index.html         # Unified Frontend (Button spamming tool)
  requirements.txt   # Dependencies
  README.md          # This file
```

## Setup and Run

### 1. Requirements

You must have **Redis** installed and running on default port `6379`.

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Start the FastAPI Server

```bash
uvicorn main:app --reload
```

### 4. Open the Frontend
Open `index.html` directly in your browser and click "Send Request" as quickly as you can!



## Example Output

```json
// After 5 fast requests:
{
  "detail": "Rate limit exceeded. Try again in 10 seconds."
}
```
## Core Concepts

- **Sliding Window Algorithm**: Unlike Fixed Window (which resets at the top of the minute), Sliding Window tracks precise timestamps. We use Redis Sorted Sets (`ZADD`, `ZREMRANGEBYSCORE`, `ZCARD`) to atomically log and count request timestamps.
- **FastAPI Dependencies**: We inject `rate_limit` directly into our routes. If the limit is exceeded, the dependency raises an `HTTPException(429)` before the route logic even begins.
- **`request.client.host`**: Identifying unique users implicitly by IP address (or could be linked to JWTs).
