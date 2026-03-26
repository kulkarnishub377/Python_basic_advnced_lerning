from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from routes import files
import os

app = FastAPI(title="File Upload & Storage API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Ensure upload directory exists before mounting
os.makedirs("uploads", exist_ok=True)

# Mount the uploads directory to serve static files
app.mount("/static", StaticFiles(directory="uploads"), name="static")

# Include the file routes
app.include_router(files.router, prefix="/api")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
