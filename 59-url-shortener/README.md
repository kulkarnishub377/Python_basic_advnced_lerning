# 59 - URL Shortener Service

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Difficulty: Advanced](https://img.shields.io/badge/Difficulty-Advanced-orange?style=for-the-badge)
![Phase](https://img.shields.io/badge/Phase-7_Expert_Projects-blue?style=for-the-badge)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)

## What It Does

A functional URL shortening backend service that takes long, cumbersome URLs and generates compact, shortened equivalents (e.g., `http://localhost:8000/x7Y9`). When a user visits the short URL, the server responds with an HTTP 307 Redirect to send them to the original destination. It includes a sleek, modern Vanilla HTML/CSS/JS frontend to interact with the API.

## Project Structure

```text
59-url-shortener/
  main.py              # FastAPI server handling creation and redirection
  urls.db              # SQLite database (auto-generated) storing the mappings
  requirements.txt     # Python dependencies
  frontend/
    index.html         # URL shortener UI structure
    style.css          # Modern glassmorphism styling
    app.js             # API integration logic
  README.md            # This file
```

## Setup and Run

### 1. Backend Setup

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

### 2. Frontend Setup

Simply open `frontend/index.html` in your web browser. Or using a local server:
```bash
cd frontend
python -m http.server 5500
```

## Core Concepts

- **Base62 Encoding**: Converting integer database IDs into short alphanumeric strings (A-Z, a-z, 0-9)
- **HTTP Redirects**: Returning status code `307 Temporary Redirect`
- **FastAPI Path Operations**: Catching the root path variable `/{short_id}`
- **SQLite Database**: Storing mapping of `id -> original_url`

## What You Will Learn

You will learn system design principles for building a classic interview project: the URL Shortener. You'll understand how databases, string encoding algorithms, and HTTP protocol redirects work together to provide a seamless user experience.

## Example Output

```text
Server log:
INFO:     Uvicorn running on http://127.0.0.1:8000
INFO:     POST /api/shorten -> Returned short_url: http://127.0.0.1:8000/B
INFO:     GET /B -> 307 Redirect to https://www.verylongdomainname.com/article/123
```
