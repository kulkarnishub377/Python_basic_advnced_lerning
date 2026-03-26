# 55 - Full-Stack Task Management API (Capstone Project)

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Difficulty: Expert](https://img.shields.io/badge/Difficulty-Expert-red?style=for-the-badge)
![Phase](https://img.shields.io/badge/Phase-7_Expert_Projects-blue?style=for-the-badge)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)

## What It Does

A production-grade Task Management REST API built with FastAPI and SQLite, paired with a dynamic Vanilla HTML/CSS/JS frontend. This capstone project brings together everything learned across the previous 54 projects into a single, cohesive full-stack application.

The application provides:
- A responsive, glassmorphic dashboard UI
- Full CRUD (Create, Read, Update, Delete) for tasks via API calls
- Dashboard analytics with aggregate statistics
- Keyword search across task titles and descriptions
- Health monitoring endpoint for uptime and database connectivity
- Pydantic-validated request/response models
- Database seeder for development and demo data
- Comprehensive test suite with pytest

## Project Structure

```text
55-capstone-project/
  backend/
    main.py              # Application entry point with factory pattern
    config.py            # Centralized configuration settings
    models.py            # Pydantic data models and enums
    database.py          # SQLite database layer with CRUD operations
    routes.py            # API route handlers (tasks, dashboard, health)
    seed.py              # Database seeder with sample data
    test_api.py          # Pytest test suite for all endpoints
    requirements.txt     # Python dependencies
  frontend/
    index.html           # Main UI structure
    style.css            # Custom CSS styling
    app.js               # Vanilla JS logic interfacing with backend API
  README.md              # This file
```

## Setup and Run

### 1. Backend Setup

```bash
cd backend
pip install -r requirements.txt
python seed.py
uvicorn main:app --reload
```

### 2. Frontend Setup

Simply open `frontend/index.html` in your web browser. Or using a local server:
```bash
cd ../frontend
python -m http.server 5500
# Then open http://127.0.0.1:5500 in your browser
```

### 4. Open the API documentation

- Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

### 5. Run the test suite

```bash
pytest test_api.py -v
```

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Root endpoint with API metadata |
| GET | `/api/health` | Health check (status, uptime, DB connectivity) |
| GET | `/api/dashboard` | Aggregate task statistics |
| POST | `/api/tasks` | Create a new task |
| GET | `/api/tasks` | List all tasks (with filters and pagination) |
| GET | `/api/tasks/{id}` | Get a specific task by ID |
| PUT | `/api/tasks/{id}` | Update a task (partial updates supported) |
| DELETE | `/api/tasks/{id}` | Delete a task |
| GET | `/api/tasks/search/{keyword}` | Search tasks by keyword |

### Query Parameters for `GET /api/tasks`

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `status` | string | null | Filter by status (pending, in_progress, completed, cancelled) |
| `priority` | string | null | Filter by priority (low, medium, high, critical) |
| `limit` | int | 50 | Results per page (1-200) |
| `offset` | int | 0 | Number of results to skip |

### Example: Create a Task

```bash
curl -X POST http://127.0.0.1:8000/api/tasks \
  -H "Content-Type: application/json" \
  -d '{"title": "Write documentation", "priority": "high", "assigned_to": "Alice"}'
```

### Example: Get Dashboard Stats

```bash
curl http://127.0.0.1:8000/api/dashboard
```

Response:

```json
{
  "total_tasks": 10,
  "pending_tasks": 6,
  "in_progress_tasks": 2,
  "completed_tasks": 1,
  "cancelled_tasks": 1,
  "high_priority_count": 4,
  "completion_rate": 10.0
}
```



## Example Output

```text
$ python main.py
> System initialized.
> Waiting for user input...
> Process complete.
```
## Core Concepts

- **Application Factory Pattern**: `create_app()` builds the FastAPI instance with middleware and routes
- **Pydantic Models**: Strict request/response validation with `BaseModel`, `Field`, and `Enum`
- **SQLite Database Layer**: Raw SQL with `sqlite3`, parameterized queries, and connection management
- **API Router**: Route separation using `APIRouter` with prefix and tags
- **CORS Middleware**: Cross-origin configuration for frontend communication
- **Pytest Testing**: `TestClient` for endpoint testing with fixtures and clean database state
- **Configuration Management**: Centralized settings with a `Settings` class
- **Database Seeding**: Reproducible sample data for development and demos
- **HTTP Status Codes**: Proper 201 (Created), 204 (No Content), 404 (Not Found), 422 (Validation Error)
- **Partial Updates**: PUT endpoint accepts optional fields, only updating what is provided

## What You Will Learn

This capstone project teaches you how to architect a complete backend application from scratch. You will understand how all the concepts from the previous 54 projects come together: classes and data models (from OOP projects), database operations (from the DB migration project), API design (from the FastAPI project), testing patterns (from pytest), configuration management, error handling with custom HTTP responses, and structuring a multi-file Python application for maintainability and scalability.

## Technologies Used

| Technology | Purpose |
|-----------|---------|
| FastAPI | Web framework for building the REST API |
| Pydantic | Data validation and serialization |
| SQLite | Lightweight embedded database |
| Uvicorn | ASGI server for running the application |
| Pytest | Testing framework for endpoint verification |
| HTTPX | HTTP client used by FastAPI's TestClient |

## Project Structure

```text
55-capstone-project/
  README.md
  backend/
    config.py
    database.py
    main.py
    models.py
    requirements.txt
    routes.py
    seed.py
    test_api.py
```
