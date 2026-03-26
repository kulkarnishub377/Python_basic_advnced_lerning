# 64 - Background Tasks & Celery

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Difficulty: Expert](https://img.shields.io/badge/Difficulty-Expert-red?style=for-the-badge)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Redis](https://img.shields.io/badge/Redis-DC382D?style=for-the-badge&logo=redis&logoColor=white)

## What It Does

This project demonstrates how to offload slow, heavy tasks (like generating ML models, sending batch emails, or processing video) away from the main FastAPI server so the user doesn't experience a stalled HTTP request. It utilizes **Celery** as the asynchronous task queue/job queue, and **Redis** as the message broker.

## Project Structure

```text
64-fastapi-celery/
  main.py            # FastAPI Entry point
  celery_app.py      # Celery worker configuration
  tasks.py           # The heavy, time-consuming functions
  index.html         # Unified Frontend (triggers task & polls status)
  requirements.txt   # Dependencies
  README.md          # This file
```

## Setup and Run

### 1. Requirements

You must have **Redis** installed and running on default port `6379`.
(For Windows: WSL, or Docker `docker run -p 6379:6379 -d redis`).

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Start the Celery Worker (Terminal 1)

```bash
celery -A celery_app worker --loglevel=info
```

*(On Windows, you may need a workaround pool: `celery -A celery_app worker --pool=solo --loglevel=info`)*

### 4. Start the FastAPI Server (Terminal 2)

```bash
uvicorn main:app --reload
```

### 5. Open the Frontend
Open `index.html` directly in your browser.



## Example Output

```json
{
  "task_id": "4b92b604-5e58-45a7-96a1-cb9daedeaebe",
  "status": "Processing",
  "message": "Task received and is running. Check /status/{task_id}"
}
```
## Core Concepts

- **Message Broker**: FastAPI doesn't talk to workers directly. It pushes a message onto a Redis queue.
- **Celery Workers**: Independent processes that listen to the Redis queue, pop messages, and execute the heavy Python logic defined in `tasks.py`.
- **Async Polling**: The frontend fires an HTTP request, receives an immediate `task_id`, and then uses JS `setInterval` to ask FastAPI for the status of that `task_id` every second.
