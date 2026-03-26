# 53 - Async Web Crawler

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Difficulty: Expert](https://img.shields.io/badge/Difficulty-Expert-red?style=for-the-badge)
![Phase](https://img.shields.io/badge/Phase-7_-_Expert_Projects-blue?style=for-the-badge)

## What It Does

An asynchronous web crawler that discovers and follows links using asyncio and aiohttp with depth limiting and URL deduplication.

## Run It

```bash
pip install -r requirements.txt
python crawler.py
```

## Core Concepts

- `asyncio` and `aiohttp` for concurrent crawling
- URL deduplication with sets
- Depth-limited BFS traversal
- HTML link extraction with regex
- Configurable crawl parameters

## What You Will Learn

You will learn building high-performance web crawlers and managing concurrent network requests.

## Project Structure

```text
53-async-crawler/
  README.md
  crawler.py
  requirements.txt
```


## Prerequisites

Install the required packages before running:

```bash
pip install aiohttp
```


## Example Output

```
Async Web Crawler
-----------------
Starting crawl from: https://example.com
Max depth: 2

[Depth 0] https://example.com - 200 (3 links found)
[Depth 1] https://example.com/about - 200 (5 links found)
[Depth 1] https://example.com/contact - 200 (2 links found)
[Depth 2] https://example.com/blog - 200 (8 links found)

Crawled 12 pages in 1.8 seconds
Unique URLs discovered: 34
```
