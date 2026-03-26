# 76 - Advanced Web Scraping (Playwright + Async)

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Difficulty: Expert](https://img.shields.io/badge/Difficulty-Expert-red?style=for-the-badge)
![Playwright](https://img.shields.io/badge/Playwright-2EAD33?style=for-the-badge&logo=playwright&logoColor=white)

## What It Does

Goes beyond traditional `requests + BeautifulSoup` scraping by using **Playwright** for headless browser automation. This project can scrape JavaScript-rendered Single Page Applications (SPAs) that server-side HTTP requests cannot access. It includes async page navigation, element waiting, and DOM extraction logic exposed through a FastAPI endpoint.

## Project Structure

```text
76-playwright-scraper/
  main.py            # FastAPI entry point with scrape endpoint
  scraper.py         # Async Playwright browser automation logic
  parser.py          # HTML parsing and data extraction utilities
  config.py          # Browser config (headless mode, timeout)
  requirements.txt   # Dependencies
  index.html         # Unified frontend to submit URLs and view results
  README.md          # This file
```

## Setup and Run

### 1. Install dependencies
```bash
pip install -r requirements.txt
playwright install chromium
```

### 2. Start the server
```bash
uvicorn main:app --reload
```

### 3. Open the Frontend
Open `index.html` and paste a URL to scrape.

## Example Output

```json
// POST /scrape  {"url": "https://example.com"}
{
  "url": "https://example.com",
  "title": "Example Domain",
  "meta_description": "This domain is for use in illustrative examples.",
  "headings": ["Example Domain"],
  "links_count": 1,
  "word_count": 28,
  "load_time_ms": 834
}
```

## Core Concepts

- **Headless Browser**: Chromium runs invisibly in the background, executing JavaScript just like a real user.
- **Async Context Manager**: `async with async_playwright() as p:` ensures clean browser lifecycle management.
- **Element Waiting**: `page.wait_for_selector()` pauses until dynamic content loads.
- **DOM Extraction**: Access `page.content()` to get the fully rendered HTML after JS execution.
