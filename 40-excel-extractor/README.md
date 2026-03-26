# 40 - Excel Data Extractor

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Difficulty: Intermediate](https://img.shields.io/badge/Difficulty-Intermediate-yellow?style=for-the-badge)
![Phase](https://img.shields.io/badge/Phase-5_-_Libraries_and_APIs-blue?style=for-the-badge)

## What It Does

Extracts and processes data from Excel spreadsheets using Pandas with filtering, column selection, and multi-format export.

## Run It

```bash
pip install -r requirements.txt
python extractor.py
```

## Core Concepts

- `pandas.read_excel()` for spreadsheet parsing
- DataFrame filtering and selection
- Data type conversion and cleaning
- Export to CSV and JSON
- Summary statistics generation

## What You Will Learn

You will learn how to process Excel data programmatically and perform transformations with Pandas.

## Project Structure

```text
40-excel-extractor/
  README.md
  extractor.py
  requirements.txt
```


## Prerequisites

Install the required packages before running:

```bash
pip install pandas, openpyxl
```


## Example Output

```
Excel Data Extractor
--------------------
Loaded: sales_data.xlsx
Sheets found: ['Q1', 'Q2', 'Q3', 'Q4']
Total rows: 1,240

Summary Statistics:
  Total Revenue: $2,340,000
  Average Order: $1,887
  Top Product: Widget Pro (342 orders)

Exported to: output.csv
```
