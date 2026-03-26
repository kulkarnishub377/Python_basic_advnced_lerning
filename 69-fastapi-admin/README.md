# 69 - FastAPI Admin Dashboard

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Difficulty: Intermediate](https://img.shields.io/badge/Difficulty-Intermediate-yellow?style=for-the-badge)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)

## What It Does

Demonstrates how to instantly generate a fully-featured, production-ready Content Management System (CMS) / Admin UI for your FastAPI backend using the `sqladmin` package. It introspects your SQLAlchemy models and automatically generates forms, tables, and search functionalities for database operations, directly accessible at `/admin`.

## Project Structure

```text
69-fastapi-admin/
  main.py            # FastAPI Entry point
  database.py        # SQLAlchemy engine and session setup
  models.py          # SQLAlchemy target tables
  admin.py           # SQLAdmin view configurations
  index.html         # A basic landing page explaining the setup
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
Open `index.html` to see the landing page, then click the link to navigate to `http://127.0.0.1:8000/admin`.



## Example Output

```text
$ uvicorn main:app
INFO:     Started server process [12345]
INFO:     Application startup complete.
INFO:     Uvicorn running on http://127.0.0.1:8000

# Navigating to http://127.0.0.1:8000/admin loads the SQLAdmin CMS interface, allowing you to instantly Create, Read, Update, and Delete Models (Categories and Posts) via a graphical user interface without writing any frontend code.
```
## Core Concepts

- **SQLAdmin Integration**: Passing the `FastAPI` app instance and the `SQLAlchemy` engine to the `Admin()` factory.
- **ModelViews**: Creating classes that inherit from `ModelView` to customize exactly which columns are visible, searchable, or editable in the auto-generated UI.
