# 20 - Library Book Tracker

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Difficulty: Intermediate](https://img.shields.io/badge/Difficulty-Intermediate-yellow?style=for-the-badge)
![Phase](https://img.shields.io/badge/Phase-3_-_File_Handling-blue?style=for-the-badge)
![UI: Streamlit](https://img.shields.io/badge/UI-Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)

## What It Does

A library management system with Streamlit dashboard. Tracks books with title, author, ISBN, and checkout status.

## Run It

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Core Concepts

- Class-based models (`Book`, `Library`)
- Streamlit dashboard with tabs
- Pandas DataFrame display
- JSON data persistence
- OOP library management logic

## What You Will Learn

You will learn building complete management applications with OOP models and web interfaces.

## Project Structure

```text
20-library-tracker/
  README.md
  app.py
  book.py
  library.py
  requirements.txt
```


## Prerequisites

Install the required packages before running:

```bash
pip install streamlit, pandas
```


## Example Output

```
Streamlit dashboard at http://localhost:8501
Features:
  - Add books with title, author, and ISBN
  - Check out and return books
  - Track overdue books
  - Search by title or author
```
