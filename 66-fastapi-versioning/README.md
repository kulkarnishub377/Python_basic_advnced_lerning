# 66 - API Versioning

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Difficulty: Intermediate](https://img.shields.io/badge/Difficulty-Intermediate-yellow?style=for-the-badge)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)

## What It Does

Demonstrates how to structure a FastAPI application to support multiple API versions concurrently. When breaking changes must be made to an API (like restructuring the response JSON), creating a `v2` router allows new clients to use the new features while legacy clients continue using `v1` without breaking. Includes a unified frontend dashboard to visualize the difference between the two versions.

## Project Structure

```text
66-fastapi-versioning/
  main.py            # FastAPI Entry point
  api/
    v1/
      routes.py      # Legacy v1 endpoints
    v2/
      routes.py      # New v2 endpoints
  index.html         # Unified Frontend to compare v1 vs v2
  requirements.txt   # Dependencies
  README.md          # This file
```

## Setup and Run

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Start the FastAPI Server

```bash
uvicorn main:app --reload
```

### 3. Open the Frontend
Open `index.html` directly in your browser to test calling `/api/v1/users` vs `/api/v2/users`.



## Example Output

```json
// GET /api/v1/users
{
  "version": "v1",
  "data": [{"id": 1, "name": "John Doe", "email": "john@example.com"}]
}

// GET /api/v2/users
{
  "version": "v2",
  "data": [{"id": 1, "first_name": "John", "last_name": "Doe", "email": "john@example.com", "is_active": true}]
}
```
## Core Concepts

- **APIRouter**: FastAPIs method for breaking up large applications.
- **Prefixes**: Mapping routers to physical URL paths like `prefix="/api/v1"`.
- **Schema Evolution**: Observing how data structures change (e.g., flattening a name into `first_name` and `last_name`) while maintaining backward compatibility.
