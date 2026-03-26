# 78 - Geospatial API (Haversine Distance)

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Difficulty: Expert](https://img.shields.io/badge/Difficulty-Expert-red?style=for-the-badge)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)

## What It Does

Simulates a location-based service (like Uber or a restaurant finder). Stores a set of Points of Interest (POIs) with latitude/longitude coordinates, then exposes an API to query which POIs fall within a given search radius using the **Haversine formula** for great-circle distance on a sphere.

## Project Structure

```text
78-geospatial-api/
  main.py            # FastAPI entry point with geo endpoints
  geo.py             # Haversine distance calculation engine
  models.py          # Pydantic models for locations
  seed_data.py       # Mock POI seeder
  database.py        # In-memory location store
  requirements.txt   # Dependencies
  index.html         # Interactive map-style frontend
  README.md          # This file
```

## Setup and Run

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Start the server
```bash
uvicorn main:app --reload
```

### 3. Open the Frontend
Open `index.html` in your browser. Click on the canvas to set a search center and adjust the radius.

## Example Output

```json
// GET /nearby?lat=19.076&lon=72.877&radius_km=5
{
  "center": {"lat": 19.076, "lon": 72.877},
  "radius_km": 5,
  "results": [
    {"name": "Gateway of India", "lat": 18.922, "lon": 72.834, "distance_km": 17.4},
    {"name": "Marine Drive", "lat": 18.943, "lon": 72.823, "distance_km": 15.2}
  ],
  "total_found": 2
}
```

## Core Concepts

- **Haversine Formula**: Calculates the shortest distance between two points on a sphere using their latitudes and longitudes.
- **Spatial Filtering**: Only returns points that fall inside the search circle.
- **GeoJSON**: Industry-standard format for encoding geographic data structures.
