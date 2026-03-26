# 54 - Custom WSGI Web Framework

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Difficulty: Expert](https://img.shields.io/badge/Difficulty-Expert-red?style=for-the-badge)
![Phase](https://img.shields.io/badge/Phase-7_-_Expert_Projects-blue?style=for-the-badge)

## What It Does

A minimal web framework built from scratch implementing the WSGI spec with URL routing, request/response objects, middleware, and template rendering.

## Run It

```bash
pip install -r requirements.txt
python framework.py
```

## Core Concepts

- WSGI application interface
- URL routing with pattern matching
- Request and Response abstraction
- Middleware pipeline architecture
- `wsgiref` development server

## What You Will Learn

You will learn how web frameworks work internally and the WSGI standard powering Python web apps.

## Project Structure

```text
54-custom-framework/
  README.md
  framework.py
```


## Example Output

```
Custom WSGI Framework
---------------------
Registered routes:
  GET  /          -> home_handler
  GET  /about     -> about_handler
  POST /api/data  -> data_handler

Serving on http://127.0.0.1:8080

$ curl http://127.0.0.1:8080/
-> 200 OK: Welcome to the custom framework!

$ curl http://127.0.0.1:8080/about
-> 200 OK: About page content
```
