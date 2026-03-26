# 47 - FastAPI REST Service

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Difficulty: Advanced](https://img.shields.io/badge/Difficulty-Advanced-orange?style=for-the-badge)
![Phase](https://img.shields.io/badge/Phase-6_-_Advanced_Concepts-blue?style=for-the-badge)

## What It Does

A RESTful API service with FastAPI featuring CRUD endpoints, Pydantic validation, automatic OpenAPI docs, and async handlers.

## Run It

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

## Core Concepts

- FastAPI routing and endpoints
- Pydantic models for validation
- CRUD endpoint design
- Automatic OpenAPI/Swagger docs
- Async endpoint handlers

## What You Will Learn

You will learn how to build production-quality REST APIs with automatic validation and documentation.

## Project Structure

```text
47-fastapi-service/
  README.md
  main.py
  requirements.txt
```


## Prerequisites

Install the required packages before running:

```bash
pip install fastapi, uvicorn
```


## Example Output

```
FastAPI Service
---------------
INFO:     Uvicorn running on http://127.0.0.1:8000
INFO:     Application startup complete.

Endpoints:
  GET  /items      - List all items
  POST /items      - Create an item
  GET  /items/{id} - Get item by ID
  PUT  /items/{id} - Update an item
  DELETE /items/{id} - Delete an item

Docs: http://127.0.0.1:8000/docs
```
