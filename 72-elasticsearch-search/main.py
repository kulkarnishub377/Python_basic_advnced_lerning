from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from search import search_products, ES_AVAILABLE

app = FastAPI(title="Elasticsearch Full-Text Search API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/search")
def search(q: str = Query(..., min_length=1, description="Search query")):
    """
    Search products using Elasticsearch fuzzy multi-match.
    Handles typos, partial matches, and ranks by relevance.
    """
    results = search_products(q)
    results["query"] = q
    return results


@app.get("/health")
def health():
    return {"elasticsearch_available": ES_AVAILABLE}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
