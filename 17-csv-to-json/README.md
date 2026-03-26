# 17 - CSV to JSON Converter

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Difficulty: Intermediate](https://img.shields.io/badge/Difficulty-Intermediate-yellow?style=for-the-badge)
![Phase](https://img.shields.io/badge/Phase-3_-_File_Handling-blue?style=for-the-badge)

## What It Does

Converts CSV files to JSON format with configurable output options and custom key mapping.

## Run It

```bash
python converter.py
```

## Core Concepts

- CSV reading with `csv.DictReader`
- JSON writing with `json.dump()`
- Data format transformation
- Command-line argument handling
- Error handling for files

## What You Will Learn

You will learn data serialization between formats and building file conversion utilities.

## Project Structure

```text
17-csv-to-json/
  README.md
  converter.py
  sample.csv
```


## Example Output

```
CSV to JSON Converter
---------------------
Input:  data.csv (150 rows, 4 columns)
Output: data.json

Converted 150 records to JSON format.
File saved: data.json (12.4 KB)
```
