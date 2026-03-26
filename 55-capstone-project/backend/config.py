"""
config.py - Application configuration for the Capstone API.
Centralizes all configuration values so they can be modified
in one place without touching application logic.
"""


class Settings:
    """
    Application settings container.
    In a production application, these would be loaded from
    environment variables or a .env file.
    """

    # Application metadata
    APP_TITLE = "Task Management API"
    APP_DESCRIPTION = (
        "A full-stack task management system built with FastAPI. "
        "Provides CRUD operations for tasks, dashboard analytics, "
        "health monitoring, and search functionality."
    )
    APP_VERSION = "1.0.0"

    # Server configuration
    HOST = "127.0.0.1"
    PORT = 8000
    DEBUG = True

    # CORS - list of allowed frontend origins
    # In production, replace with specific URLs like ["https://myapp.com"]
    CORS_ORIGINS = [
        "http://localhost:3000",     # React default
        "http://localhost:5173",     # Vite default
        "http://127.0.0.1:5500",    # VS Code Live Server
    ]

    # Database
    DATABASE_NAME = "capstone.db"


# Singleton settings instance used throughout the application
settings = Settings()
