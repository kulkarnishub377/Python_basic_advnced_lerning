# 62 - JWT Authentication API

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Difficulty: Advanced](https://img.shields.io/badge/Difficulty-Advanced-orange?style=for-the-badge)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)

## What It Does

A robust authentication system built with FastAPI using JSON Web Tokens (JWT). It demonstrates how to register users, securely hash passwords using bcrypt, issue access tokens upon successful login, and protect specific API endpoints using dependency injection (`Depends(get_current_active_user)`). It includes a unified HTML/JS frontend that interacts with the authentication flow and stores the token securely in `localStorage`.

## Project Structure

```text
62-jwt-auth/
  main.py            # FastAPI Entry point
  auth.py            # Password hashing and JWT token generation
  dependencies.py    # FastAPI dependencies for extracting/verifying tokens
  routes/
    users.py         # Endpoints for register, login, & current user info
  index.html         # Unified single-file Frontend (HTML/CSS/JS)
  requirements.txt   # Dependencies
  README.md          # This file
```

## Setup and Run

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Start the Server

```bash
uvicorn main:app --reload
```

### 3. Open the Frontend
Open `index.html` directly in your browser or run a simple server:
```bash
python -m http.server 5500
```
Then navigate to `http://127.0.0.1:5500`.



## Example Output

```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "bearer"
}
```
## Core Concepts

- **OAuth2 with Password (and hashing), Bearer with JWT tokens**: Implementing standard `OAuth2PasswordBearer`.
- **Passlib & Bcrypt**: Secure one-way hashing of user passwords before saving them.
- **Python-JOSE**: Generating and signing JSON Web Tokens using HS256 algorithm.
- **FastAPI Dependencies**: Extracting the Authorization header injected directly into route handlers.
- **Unified Frontend API Flow**: Fetching the token from `/token` using `FormData` (x-www-form-urlencoded), storing it locally, and appending `Authorization: Bearer <token>` to protected API requests.
