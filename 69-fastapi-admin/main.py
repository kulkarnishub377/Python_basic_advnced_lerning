from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqladmin import Admin
from database import engine, Base
from admin import CategoryAdmin, PostAdmin

# Create the SQLite tables immediately
Base.metadata.create_all(bind=engine)

app = FastAPI(title="CMS Admin Dashboard")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize SQLAdmin using the FastAPI app and the SQLAlchemy engine
# This automatically mounts the CMS dashboard to /admin
admin = Admin(app, engine, title="FastAPI Headless CMS")

# Register our customized views
admin.add_view(CategoryAdmin)
admin.add_view(PostAdmin)

@app.get("/")
def read_root():
    return {
        "message": "Welcome to the FastAPI App",
        "admin_url": "/admin"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
