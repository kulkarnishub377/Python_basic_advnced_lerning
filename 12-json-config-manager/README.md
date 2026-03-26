# 12 - JSON Config Manager

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Difficulty: Beginner](https://img.shields.io/badge/Difficulty-Beginner-green?style=for-the-badge)
![Phase](https://img.shields.io/badge/Phase-2_-_Intermediate_Python-blue?style=for-the-badge)

## What It Does

A configuration management system using JSON files. Supports reading, writing, updating, and deleting configuration keys.

## Run It

```bash
python config.py
```

## Core Concepts

- JSON serialization with `json.load()` and `json.dump()`
- Dictionary CRUD operations
- File-based persistent configuration
- Error handling for malformed JSON
- Nested key access

## What You Will Learn

You will learn JSON file operations, dictionary manipulation, and building configuration management systems.

## Project Structure

```text
12-json-config-manager/
  README.md
  config.py
  settings.json
```


## Example Output

```
JSON Config Manager
-------------------
1. View config
2. Get key
3. Set key
4. Delete key
5. Quit

Choice: 3
Key: database.host
Value: localhost
Config updated: database.host = localhost
```
