from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from database import get_all_locations
from geo import find_within_radius
from seed_data import seed

app = FastAPI(title="Geospatial Nearby Search API")

app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

# Seed mock data on startup
seed()


@app.get("/nearby")
def nearby(
    lat: float = Query(..., description="Center latitude"),
    lon: float = Query(..., description="Center longitude"),
    radius_km: float = Query(10.0, description="Search radius in km"),
):
    """Find all POIs within the given radius from the center coordinates."""
    all_locations = get_all_locations()
    results = find_within_radius(lat, lon, radius_km, all_locations)
    return {
        "center": {"lat": lat, "lon": lon},
        "radius_km": radius_km,
        "results": results,
        "total_found": len(results),
    }


@app.get("/locations")
def all_locations():
    """Return every POI in the database."""
    return get_all_locations()


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
