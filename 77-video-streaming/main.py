import os
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import StreamingResponse, HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from config import MEDIA_DIR
from streamer import range_reader, parse_range_header
from utils import get_content_type, validate_file

app = FastAPI(title="Video Streaming Server")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

os.makedirs(MEDIA_DIR, exist_ok=True)


@app.get("/stream/{filename}")
async def stream_video(filename: str, request: Request):
    """
    Stream a video file with byte-range support.
    The browser sends Range headers automatically when using <video> elements.
    """
    filepath = os.path.join(MEDIA_DIR, filename)

    if not validate_file(filepath):
        raise HTTPException(404, f"Video '{filename}' not found in media directory")

    file_size = os.path.getsize(filepath)
    content_type = get_content_type(filename)

    range_header = request.headers.get("range")

    if range_header:
        start, end = parse_range_header(range_header, file_size)
        content_length = end - start + 1

        headers = {
            "Content-Range": f"bytes {start}-{end}/{file_size}",
            "Accept-Ranges": "bytes",
            "Content-Length": str(content_length),
            "Content-Type": content_type,
        }

        return StreamingResponse(
            range_reader(filepath, start, end),
            status_code=206,
            headers=headers,
            media_type=content_type,
        )
    else:
        # No range header: stream the entire file
        headers = {
            "Accept-Ranges": "bytes",
            "Content-Length": str(file_size),
            "Content-Type": content_type,
        }
        return StreamingResponse(
            range_reader(filepath, 0, file_size - 1),
            headers=headers,
            media_type=content_type,
        )


@app.get("/videos")
def list_videos():
    """List all available video files in the media directory."""
    files = [f for f in os.listdir(MEDIA_DIR) if os.path.isfile(os.path.join(MEDIA_DIR, f))]
    return {"videos": files}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
