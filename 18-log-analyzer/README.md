# 18 - Log File Analyzer

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Difficulty: Intermediate](https://img.shields.io/badge/Difficulty-Intermediate-yellow?style=for-the-badge)
![Phase](https://img.shields.io/badge/Phase-3_-_File_Handling-blue?style=for-the-badge)

## What It Does

Parses and analyzes log files to extract patterns, count error frequencies, and generate summary reports.

## Run It

```bash
python analyzer.py
```

## Core Concepts

- Regular expressions with `re` module
- Log file parsing line-by-line
- Frequency counting and summary stats
- Report generation (`report.py`)
- Multi-file project structure

## What You Will Learn

You will learn regex-based text parsing, log analysis, and generating analytical reports.

## Project Structure

```text
18-log-analyzer/
  README.md
  analyzer.py
  report.py
  sample.log
```


## Example Output

```
Log File Analysis Report
------------------------
File: application.log
Total lines: 5,240

Severity Breakdown:
  INFO:    3,820 (72.9%)
  WARNING:   890 (17.0%)
  ERROR:     480 (9.2%)
  CRITICAL:   50 (1.0%)

Most frequent error: ConnectionTimeout (127 occurrences)
```
