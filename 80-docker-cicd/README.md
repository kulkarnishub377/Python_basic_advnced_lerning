# 80 - CI/CD & Docker Architecture

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Difficulty: Expert](https://img.shields.io/badge/Difficulty-Expert-red?style=for-the-badge)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?style=for-the-badge&logo=githubactions&logoColor=white)

## What It Does

Demonstrates a production-ready **containerized deployment** workflow. Wraps a Python FastAPI application inside a multi-stage Docker image, orchestrates it with `docker-compose.yml` alongside a Redis cache, and includes a GitHub Actions CI/CD pipeline that automatically runs tests on every push before deployment.

## Project Structure

```text
80-docker-cicd/
  app/
    main.py           # FastAPI application
    config.py         # Environment-based configuration
    routes.py         # API route definitions
    tests/
      test_main.py    # Pytest unit tests
  Dockerfile          # Multi-stage production Docker image
  docker-compose.yml  # Multi-container orchestration (app + redis)
  .github/
    workflows/
      test.yml        # GitHub Actions CI pipeline
  requirements.txt    # Dependencies
  index.html          # Architecture diagram frontend
  README.md           # This file
```

## Setup and Run

### Option A: Run with Docker Compose
```bash
docker-compose up --build
```

### Option B: Run Locally
```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### Option C: Run Tests
```bash
pytest app/tests/ -v
```

## Example Output

```text
# docker-compose up --build
Building app...
Step 1/8 : FROM python:3.11-slim AS builder
Step 2/8 : WORKDIR /app
Step 3/8 : COPY requirements.txt .
Step 4/8 : RUN pip install --no-cache-dir -r requirements.txt
Step 5/8 : FROM python:3.11-slim
Step 6/8 : COPY --from=builder /usr/local/lib/python3.11 /usr/local/lib/python3.11
Step 7/8 : COPY app/ /app/
Step 8/8 : CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
Successfully built abc123def456
Creating docker-cicd_redis_1 ... done
Creating docker-cicd_app_1   ... done
app_1    | INFO:     Uvicorn running on http://0.0.0.0:8000

# pytest output
app/tests/test_main.py::test_health_check PASSED
app/tests/test_main.py::test_get_items PASSED
app/tests/test_main.py::test_create_item PASSED
3 passed in 0.42s
```

## Core Concepts

- **Multi-Stage Build**: Reduces final Docker image size by separating build and runtime stages.
- **Docker Compose**: Defines and runs multi-container applications with a single YAML file.
- **GitHub Actions CI**: Automatically runs `pytest` on every push/PR to catch regressions before merge.
- **Environment Variables**: `config.py` reads `REDIS_URL` from the environment, supporting both local and container modes.
- **Health Checks**: Docker and the API both expose health endpoints for monitoring.
