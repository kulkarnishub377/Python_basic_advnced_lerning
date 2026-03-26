# 45 - Async API Data Fetcher

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Difficulty: Advanced](https://img.shields.io/badge/Difficulty-Advanced-orange?style=for-the-badge)
![Phase](https://img.shields.io/badge/Phase-6_-_Advanced_Concepts-blue?style=for-the-badge)

## What It Does

Fetches data from multiple APIs concurrently using asyncio and aiohttp, demonstrating async/await patterns.

## Run It

```bash
pip install -r requirements.txt
python fetcher.py
```

## Core Concepts

- `asyncio` event loop and `async/await`
- `aiohttp` for async HTTP requests
- `asyncio.gather()` for concurrency
- Async context managers
- Sync vs async performance comparison

## What You Will Learn

You will learn asynchronous programming with asyncio and when async patterns provide significant performance benefits.

## Project Structure

```text
45-async-fetcher/
  README.md
  fetcher.py
  requirements.txt
```


## Prerequisites

Install the required packages before running:

```bash
pip install aiohttp
```


## Example Output

```
Async API Fetcher
-----------------
Fetching 10 URLs concurrently...

[1/10] https://api.example.com/users - 200 OK (0.12s)
[2/10] https://api.example.com/posts - 200 OK (0.15s)
...
[10/10] https://api.example.com/stats - 200 OK (0.09s)

All 10 requests completed in 0.31 seconds
Synchronous equivalent: ~1.5 seconds
```
