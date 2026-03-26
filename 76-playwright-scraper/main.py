from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from scraper import scrape_url

app = FastAPI(title="Playwright Async Scraper API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class ScrapeRequest(BaseModel):
    url: str


@app.post("/scrape")
async def scrape(req: ScrapeRequest):
    """Scrape a URL using headless Chromium and return extracted metadata."""
    if not req.url.startswith("http"):
        raise HTTPException(400, "URL must start with http:// or https://")

    result = await scrape_url(req.url)

    if "error" in result:
        raise HTTPException(502, result["error"])

    return result


@app.get("/health")
def health():
    return {"status": "ok"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
