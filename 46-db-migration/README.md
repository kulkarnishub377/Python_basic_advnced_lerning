# 46 - Database Migration Tool

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Difficulty: Advanced](https://img.shields.io/badge/Difficulty-Advanced-orange?style=for-the-badge)
![Phase](https://img.shields.io/badge/Phase-6_-_Advanced_Concepts-blue?style=for-the-badge)

## What It Does

A SQLite database migration system that tracks schema versions and applies incremental up/down changes.

## Run It

```bash
python migrate.py
```

## Core Concepts

- `sqlite3` module for database operations
- Schema version tracking
- SQL DDL for table creation/modification
- Up/down migration pattern
- Idempotent migration execution

## What You Will Learn

You will learn database schema management and the migration pattern used by production ORMs.

## Project Structure

```text
46-db-migration/
  README.md
  migrate.py
```


## Example Output

```
Database Migration Tool
-----------------------
Current version: 0
Available migrations: 3

Applying migration 001_create_users... OK
Applying migration 002_add_email_column... OK
Applying migration 003_create_posts... OK

Database is now at version 3.
```
