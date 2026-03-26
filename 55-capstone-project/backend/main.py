"""
Capstone Project - Full-Stack Task Management API
--------------------------------------------------
This is the main application entry point for the FastAPI backend.
It initializes the database, registers routes, and configures
CORS middleware for frontend communication.

To run:
    uvicorn main:app --reload

The API documentation is automatically available at:
    - Swagger UI: http://127.0.0.1:8000/docs
    - ReDoc:      http://127.0.0.1:8000/redoc
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes import router
from database import init_database
from config import settings


def create_app():
    """
    Application factory function.
    Creates and configures the FastAPI application instance.
    This pattern makes the app easier to test and extend.
    """
    application = FastAPI(
        title=settings.APP_TITLE,
        description=settings.APP_DESCRIPTION,
        version=settings.APP_VERSION,
        docs_url="/docs",
        redoc_url="/redoc",
    )

    # Configure CORS to allow the frontend to communicate with this backend.
    # In production, replace allow_origins with the specific frontend URL.
    application.add_middleware(
        CORSMiddleware,
        allow_origins=settings.CORS_ORIGINS,
        allow_credentials=True,
        allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
        allow_headers=["*"],
    )

    # Register the API router containing all endpoint handlers
    application.include_router(router)

    # Root endpoint - serves as a simple connectivity check
    @application.get("/")
    def root():
        """Root endpoint returning basic API information."""
        return {
            "application": settings.APP_TITLE,
            "version": settings.APP_VERSION,
            "documentation": "/docs",
            "health_endpoint": "/api/health",
        }

    return application


# Initialize the database schema on module load
init_database()

# Create the application instance
app = create_app()


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host=settings.HOST,
        port=settings.PORT,
        reload=settings.DEBUG,
    )
