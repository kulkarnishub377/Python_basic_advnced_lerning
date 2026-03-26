# 04 - Todo List Manager

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Difficulty: Beginner](https://img.shields.io/badge/Difficulty-Beginner-green?style=for-the-badge)
![Phase](https://img.shields.io/badge/Phase-1_-_Absolute_Basics-blue?style=for-the-badge)

## What It Does

A persistent command-line todo list application. Tasks are stored in a text file so they survive between sessions. Supports adding, viewing, completing, and deleting tasks.

## Run It

```bash
python todo.py
```

## Core Concepts

- File I/O with `open()`, `read()`, and `write()`
- List manipulation (append, remove, enumerate)
- Persistent data storage in plain text files
- Menu-driven CRUD operations
- String formatting for task display

## What You Will Learn

You will learn how to persist data between program runs using file I/O, perform CRUD operations on lists, and build a practical utility tool.

## Project Structure

```text
04-todo-list/
  README.md
  todo.py
```


## Example Output

```
Todo List Manager
-----------------
1. View tasks
2. Add task
3. Complete task
4. Delete task
5. Quit

Choice: 2
Enter task: Buy groceries
Task added successfully!

Choice: 1
1. [ ] Buy groceries
```
