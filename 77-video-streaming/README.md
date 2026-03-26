# 77 - Video Streaming Server

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Difficulty: Expert](https://img.shields.io/badge/Difficulty-Expert-red?style=for-the-badge)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)

## What It Does

Implements a **byte-range video streaming** server using FastAPI's `StreamingResponse`. Instead of loading entire video files into memory (which would crash the server on large files), this project reads and streams video data in configurable chunks, supporting browser-native `Range` HTTP headers for seeking, pausing, and resuming playback.

## Project Structure

```text
77-video-streaming/
  main.py            # FastAPI entry point with streaming endpoint
  streamer.py        # Byte-range file reader and chunk generator
  config.py          # Chunk size and media directory config
  utils.py           # File validation and content-type detection
  media/
    sample.mp4       # Place your video file here (not included)
  requirements.txt   # Dependencies
  index.html         # Unified HTML5 video player frontend
  README.md          # This file
```

## Setup and Run

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Add a video file
Place any `.mp4` file into the `media/` directory and name it `sample.mp4`.

### 3. Start the server
```bash
uvicorn main:app --reload
```

### 4. Open the Frontend
Open `index.html` or navigate to `http://localhost:8000` to watch the video.

## Example Output

```text
# Request with Range header
GET /stream/sample.mp4
Range: bytes=0-1048575

# Response Headers
HTTP/1.1 206 Partial Content
Content-Range: bytes 0-1048575/52428800
Content-Length: 1048576
Content-Type: video/mp4
Accept-Ranges: bytes
```

## Core Concepts

- **HTTP 206 Partial Content**: The server responds with only the requested byte range, not the full file.
- **StreamingResponse**: FastAPI yields chunks via a Python generator, keeping memory usage constant.
- **Range Headers**: The browser automatically sends `Range: bytes=X-Y` when seeking in the video player.
- **Content-Type Detection**: MIME type is inferred from the file extension for correct browser handling.
