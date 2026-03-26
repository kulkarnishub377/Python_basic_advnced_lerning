import os

REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379/0")
DEBUG = os.getenv("DEBUG", "true").lower() == "true"
APP_NAME = "Docker CI/CD Demo"
APP_VERSION = "1.0.0"
