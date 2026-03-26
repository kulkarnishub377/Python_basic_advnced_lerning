import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Fallback to sqlite if postgres is not available for easy local testing
POSTGRES_URL = "postgresql://user:password@localhost/dbname"
SQLITE_URL = "sqlite:///./sql_app.db"

# Select database URL based on environment variable (defaulting to SQLite for portability)
SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL", SQLITE_URL)

if SQLALCHEMY_DATABASE_URL.startswith("sqlite"):
    engine = create_engine(
        SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
    )
else:
    engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    """Dependency for injecting database sessions."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
