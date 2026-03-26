# 61 - FastAPI with PostgreSQL & SQLAlchemy

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Difficulty: Advanced](https://img.shields.io/badge/Difficulty-Advanced-orange?style=for-the-badge)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)

## What It Does

This project demonstrates how to connect a FastAPI backend to a relational database using the **SQLAlchemy ORM** and how to manage database schema changes using **Alembic**. While the code is configured to use PostgreSQL (via `psycopg2`), it falls back to SQLite for easy local testing if no Postgres server is running. It includes a unified HTML/JS frontend interface to manage "Items" in the database.

## Project Structure

```text
61-fastapi-postgres/
  main.py            # FastAPI application and routes
  database.py        # SQLAlchemy engine and session management
  models.py          # SQLAlchemy database models
  schemas.py         # Pydantic data validation schemas
  crud.py            # CRUD operations separating DB logic from routes
  index.html         # Unified single-file Frontend (HTML/CSS/JS)
  alembic.ini        # Alembic configuration file
  alembic/           # Alembic migration scripts directory
  requirements.txt   # Dependencies
  README.md          # This file
```

## Setup and Run

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Database Migrations (Alembic)
Instead of relying on `Base.metadata.create_all()`, we use Alembic to create the tables:
```bash
alembic upgrade head
```

### 3. Start the Server

```bash
uvicorn main:app --reload
```

### 4. Open the Frontend
Open `index.html` directly in your browser or run a simple server:
```bash
python -m http.server 5500
```
Then navigate to `http://127.0.0.1:5500`.



## Example Output

```json
[
  {
    "id": 1,
    "title": "Smartphone",
    "description": "Latest model",
    "is_active": true
  }
]
```
## Core Concepts

- **SQLAlchemy ORM**: Mapping Python classes to database tables.
- **Dependency Injection**: Injecting a database session `SessionLocal` into route handlers.
- **Alembic**: Managing schema changes over time via tracked migration scripts.
- **Pydantic Schemas**: Differentiating between generic schemas (Create/Update) and ORM-enabled schemas (Response).
- **Unified Frontend**: Using a single-file `index.html` with inline `<style>` and `<script>` containing modern styling and API fetch logic.
