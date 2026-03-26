# 63 - File Upload & S3 storage API

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Difficulty: Expert](https://img.shields.io/badge/Difficulty-Expert-red?style=for-the-badge)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)

## What It Does

A FastAPI project that handles parsing `multipart/form-data` for file uploads. It abstracts the storage layer into a repository (`storage.py`) so you can easily switch between local disk storage (for dev) and AWS S3 (for production). The web frontend features a drag-and-drop HTML5 unified interface to test file creation.

## Project Structure

```text
63-fastapi-s3-upload/
  main.py            # FastAPI Entry point
  storage.py         # Abstracted Storage layer (Local Disk vs AWS S3)
  routes/
    files.py         # Routes handling file I/O
  uploads/           # Local folder storing dev files
  index.html         # Unified single-file Frontend (Drag and drop)
  requirements.txt   # Dependencies
  README.md          # This file
```

## Setup and Run

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Start the Server

```bash
uvicorn main:app --reload
```

### 3. Open the Frontend
Open `index.html` directly in your browser. Since it operates completely client-side in terms of layout, you can just click on the file in your OS, no need for `http.server`.



## Example Output

```json
{
  "info": "2 files uploaded successfully",
  "filenames": [
    "c8a1b2_document.pdf",
    "f2e4d9_image.png"
  ]
}
```
## Core Concepts

- **FastAPI UploadFile / File**: Effectively parsing binary files.
- **`aiofiles`**: Writing binary files to local disk asynchronously so the main event loop isn't blocked.
- **Repository Pattern**: We place the actual "save logic" inside `storage.py`. Here we use local disk logic, but `boto3` for S3 is mentioned so a developer can switch depending on environment variables.
- **Serving Static Files**: Using `fastapi.staticfiles` to serve previously uploaded images.
