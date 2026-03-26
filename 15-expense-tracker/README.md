# 15 - Expense Tracker

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Difficulty: Intermediate](https://img.shields.io/badge/Difficulty-Intermediate-yellow?style=for-the-badge)
![Phase](https://img.shields.io/badge/Phase-2_-_Intermediate_Python-blue?style=for-the-badge)

## What It Does

A personal finance tracking tool with category-based expense management, monthly summaries, and CSV export.

## Run It

```bash
python tracker.py
```

## Core Concepts

- Date handling with `datetime`
- Category-based data organization
- Monthly and category aggregation
- CSV export for spreadsheets
- Utility module separation (`utils.py`)

## What You Will Learn

You will learn date-based filtering, data aggregation patterns, and multi-file project structure.

## Project Structure

```text
15-expense-tracker/
  README.md
  data/
    expenses.json
  tracker.py
  utils.py
```


## Example Output

```
Expense Tracker
---------------
1. Add Expense
2. View Monthly Summary
3. View by Category
4. Export to CSV
5. Quit

Choice: 1
Amount: 45.50
Category: Food
Description: Lunch
Expense added: $45.50 [Food]
```
