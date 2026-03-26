# 48 - Web Scraper Dashboard

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Difficulty: Advanced](https://img.shields.io/badge/Difficulty-Advanced-orange?style=for-the-badge)
![Phase](https://img.shields.io/badge/Phase-6_-_Advanced_Concepts-blue?style=for-the-badge)
![UI: Streamlit](https://img.shields.io/badge/UI-Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)

## What It Does

A web scraper that extracts headers and links from webpages using BeautifulSoup with a Streamlit dashboard and CSV export.

## Run It

```bash
pip install -r requirements.txt
streamlit run scraper.py
```

## Core Concepts

- `BeautifulSoup` for HTML parsing
- `requests` with custom headers
- HTML element extraction
- Pandas DataFrame display
- CSV export with download buttons

## What You Will Learn

You will learn web scraping fundamentals, HTML parsing, and building data extraction tools.

## Project Structure

```text
48-weather-scraper/
  README.md
  requirements.txt
  scraper.py
```


## Prerequisites

Install the required packages before running:

```bash
pip install streamlit, requests, beautifulsoup4, pandas
```


## Example Output

```
Streamlit dashboard at http://localhost:8501
Features:
  - Enter any URL to scrape
  - Extracts all headings (H1, H2, H3)
  - Counts total links on the page
  - Export results as CSV
```
