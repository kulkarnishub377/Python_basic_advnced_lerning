# 72 - Elasticsearch Full-Text Search

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Difficulty: Expert](https://img.shields.io/badge/Difficulty-Expert-red?style=for-the-badge)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Elasticsearch](https://img.shields.io/badge/Elasticsearch-005571?style=for-the-badge&logo=elasticsearch&logoColor=white)

## What It Does

Implements a **full-text search engine** powered by Elasticsearch. The application loads mock product data into an Elasticsearch index, then exposes an API endpoint that accepts a search query and returns fuzzy-matched, typo-tolerant results ranked by relevance score. Includes a Google-style live search frontend.

## Project Structure

```text
72-elasticsearch-search/
  main.py            # FastAPI entry point with search endpoints
  search.py          # Elasticsearch client, indexing & query logic
  seed_data.py       # Script to load mock products into the index
  requirements.txt   # Dependencies
  index.html         # Unified live-search frontend
  README.md          # This file
```

## Setup and Run

### Prerequisites
- Elasticsearch 8.x running locally on port 9200

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Seed the Elasticsearch index
```bash
python seed_data.py
```

### 3. Start the FastAPI server
```bash
uvicorn main:app --reload
```

### 4. Open the Frontend
Open `index.html` in your browser and start typing to search.

## Example Output

```json
// GET /search?q=laptp (typo-tolerant!)
{
  "query": "laptp",
  "total_hits": 2,
  "results": [
    {
      "name": "Gaming Laptop Pro",
      "category": "Electronics",
      "price": 1499.99,
      "score": 4.82
    },
    {
      "name": "Ultrabook Laptop 14",
      "category": "Electronics",
      "price": 899.99,
      "score": 4.15
    }
  ]
}
```

## Core Concepts

- **Full-Text Search**: Unlike SQL `LIKE`, Elasticsearch tokenizes, stems, and ranks results by relevance.
- **Fuzzy Matching**: Handles typos using Levenshtein distance (e.g., "laptp" matches "laptop").
- **Inverted Index**: Elasticsearch builds an inverted index for lightning-fast lookups.
- **Relevance Scoring**: Each result has a `_score` representing how well it matches the query.
