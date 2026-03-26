# 24 - Python Decorators

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Difficulty: Intermediate](https://img.shields.io/badge/Difficulty-Intermediate-yellow?style=for-the-badge)
![Phase](https://img.shields.io/badge/Phase-4_-_OOP_and_Data_Structures-blue?style=for-the-badge)

## What It Does

A showcase of Python decorators including timing, logging, retry, and memoization decorators with both function and class patterns.

## Run It

```bash
python examples.py
```

## Core Concepts

- Function decorators with `@` syntax
- Decorator factories with arguments
- `functools.wraps` pattern
- Timing and logging decorators
- Retry decorator with configurable attempts

## What You Will Learn

You will learn how decorators work, when to use them, and how to build reusable decorators for cross-cutting concerns.

## Project Structure

```text
24-decorators/
  README.md
  decorators.py
  examples.py
```


## Example Output

```
Decorator Showcase
------------------
[TIMER] slow_function took 2.003 seconds
[LOG] add(3, 5) called -> returned 8
[RETRY] Attempt 1 failed: Connection error
[RETRY] Attempt 2 succeeded
[CACHE] fibonacci(10) computed -> 55
[CACHE] fibonacci(10) returned cached -> 55
```
