# 43 - Multi-Threaded File Downloader

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Difficulty: Advanced](https://img.shields.io/badge/Difficulty-Advanced-orange?style=for-the-badge)
![Phase](https://img.shields.io/badge/Phase-6_-_Advanced_Concepts-blue?style=for-the-badge)

## What It Does

Downloads multiple files concurrently using Python threading with progress tracking, configurable thread count, and retry logic.

## Run It

```bash
pip install -r requirements.txt
python downloader.py
```

## Core Concepts

- `threading.Thread` for concurrent downloads
- `requests` for HTTP file downloads
- Thread synchronization and progress
- Retry logic with backoff
- Chunked file writing

## What You Will Learn

You will learn multi-threaded programming and how to speed up I/O-bound tasks with concurrency.

## Project Structure

```text
43-threaded-downloader/
  README.md
  downloader.py
```


## Prerequisites

Install the required packages before running:

```bash
pip install requests
```


## Example Output

```
Multi-Threaded Downloader
-------------------------
Downloading 5 files with 3 threads...

[Thread-1] file1.zip: 100% (2.3 MB)
[Thread-2] file2.zip: 100% (1.8 MB)
[Thread-3] file3.zip: 100% (4.1 MB)
[Thread-1] file4.zip: 100% (0.9 MB)
[Thread-2] file5.zip: 100% (3.2 MB)

All 5 files downloaded in 4.2 seconds.
```
