# 26 - Context Managers

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Difficulty: Intermediate](https://img.shields.io/badge/Difficulty-Intermediate-yellow?style=for-the-badge)
![Phase](https://img.shields.io/badge/Phase-4_-_OOP_and_Data_Structures-blue?style=for-the-badge)

## What It Does

Demonstrates Python context managers using class-based and decorator-based approaches for file handling, database connections, and timers.

## Run It

```bash
python examples.py
```

## Core Concepts

- Class-based `__enter__` and `__exit__` methods
- Decorator-based context managers with `contextlib`
- Resource cleanup and exception handling
- Timer context manager for benchmarking
- The `with` statement protocol

## What You Will Learn

You will learn how context managers automate resource management and prevent resource leaks.

## Project Structure

```text
26-context-managers/
  README.md
  examples.py
  managers.py
```


## Example Output

```
Context Manager Demo
--------------------
[FileManager] Opening data.txt
File content: Hello, World!
[FileManager] Closing data.txt

[Timer] Code block took 0.502 seconds

[DatabaseConnection] Connected
Query executed successfully
[DatabaseConnection] Disconnected
```
