import sqlite3
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, HttpUrl
import string

app = FastAPI(title="URL Shortener API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- Database Setup ---
DB_FILE = "urls.db"

def get_db():
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row
    return conn

# Initialize table
with get_db() as conn:
    conn.execute("""
        CREATE TABLE IF NOT EXISTS urls (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            original_url TEXT NOT NULL UNIQUE,
            clicks INTEGER DEFAULT 0
        )
    """)

# --- Base62 Conversion ---
BASE62_ALPHABET = string.digits + string.ascii_letters

def encode_base62(num: int) -> str:
    """Encodes a base 10 integer to base 62 string."""
    if num == 0:
        return BASE62_ALPHABET[0]
    
    encoded = []
    base = len(BASE62_ALPHABET)
    while num > 0:
        rem = num % base
        encoded.append(BASE62_ALPHABET[rem])
        num = num // base
    
    return "".join(reversed(encoded))

def decode_base62(short_str: str) -> int:
    """Decodes a base 62 string to a base 10 integer."""
    base = len(BASE62_ALPHABET)
    num = 0
    for char in short_str:
        num = num * base + BASE62_ALPHABET.index(char)
    return num


# --- Pydantic Models ---
class URLCreateRequest(BaseModel):
    url: HttpUrl

class URLResponse(BaseModel):
    original_url: str
    short_url: str


# --- API Endpoints ---
@app.post("/api/shorten", response_model=URLResponse)
def create_short_url(request_data: URLCreateRequest, request: Request):
    """
    Accepts a long URL and generates a short Base62 equivalent.
    """
    long_url = str(request_data.url)
    
    with get_db() as conn:
        # Check if URL already exists
        cursor = conn.execute("SELECT id FROM urls WHERE original_url = ?", (long_url,))
        row = cursor.fetchone()
        
        if row:
            db_id = row["id"]
        else:
            # Insert new URL
            cursor = conn.execute("INSERT INTO urls (original_url) VALUES (?)", (long_url,))
            conn.commit()
            db_id = cursor.lastrowid
            
    short_code = encode_base62(db_id)
    
    # Construct total short URL (e.g. http://127.0.0.1:8000/aB3)
    base_url = str(request.base_url)
    return URLResponse(
        original_url=long_url,
        short_url=f"{base_url}{short_code}"
    )


@app.get("/{short_code}")
def redirect_to_url(short_code: str):
    """
    Accepts the short code, decodes it, and redirects the user
    to the original long URL.
    """
    try:
        db_id = decode_base62(short_code)
    except ValueError:
        raise HTTPException(status_code=404, detail="Invalid short code")
        
    with get_db() as conn:
        cursor = conn.execute("SELECT original_url FROM urls WHERE id = ?", (db_id,))
        row = cursor.fetchone()
        
        if row:
            # Update analytics
            conn.execute("UPDATE urls SET clicks = clicks + 1 WHERE id = ?", (db_id,))
            conn.commit()
            
            # Perform redirect
            return RedirectResponse(url=row["original_url"], status_code=307)
        else:
            raise HTTPException(status_code=404, detail="URL not found")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
