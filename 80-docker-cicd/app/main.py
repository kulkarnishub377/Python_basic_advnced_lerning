from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config import APP_NAME, APP_VERSION
from app.routes import router

app = FastAPI(title=APP_NAME, version=APP_VERSION)

app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

app.include_router(router, prefix="/api")


@app.get("/health")
def health():
    return {"status": "healthy", "app": APP_NAME, "version": APP_VERSION}
