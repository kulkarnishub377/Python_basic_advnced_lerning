# 50 - Flask REST API with Auth

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Difficulty: Expert](https://img.shields.io/badge/Difficulty-Expert-red?style=for-the-badge)
![Phase](https://img.shields.io/badge/Phase-7_-_Expert_Projects-blue?style=for-the-badge)

## What It Does

A Flask-based REST API with JWT authentication, user registration, login, and protected endpoints.

## Run It

```bash
pip install -r requirements.txt
python app.py
```

## Core Concepts

- Flask application factory pattern
- JWT token generation and validation
- Password hashing with werkzeug
- Protected routes with auth decorators
- RESTful endpoint design

## What You Will Learn

You will learn how to build authenticated REST APIs with JWT token flows and security best practices.

## Project Structure

```text
50-flask-rest-api/
  README.md
  app.py
  requirements.txt
```


## Prerequisites

Install the required packages before running:

```bash
pip install flask
```


## Example Output

```
Flask REST API
--------------
 * Running on http://127.0.0.1:5000

Endpoints:
  POST /register  - Register new user
  POST /login     - Get JWT token
  GET  /protected - Access protected resource (requires token)
  GET  /users     - List all users (admin only)

Example:
  curl -X POST /login -d '{"username":"admin","password":"secret"}'
  -> {"token": "eyJhbGciOi..."}
```
