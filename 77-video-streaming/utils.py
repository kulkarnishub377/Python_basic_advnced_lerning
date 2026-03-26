import os

MIME_TYPES = {
    ".mp4": "video/mp4",
    ".webm": "video/webm",
    ".ogg": "video/ogg",
    ".avi": "video/x-msvideo",
    ".mkv": "video/x-matroska",
}


def get_content_type(filename: str) -> str:
    """Detect MIME type from file extension."""
    ext = os.path.splitext(filename)[1].lower()
    return MIME_TYPES.get(ext, "application/octet-stream")


def validate_file(filepath: str) -> bool:
    """Check that the file exists and is a supported video format."""
    if not os.path.isfile(filepath):
        return False
    ext = os.path.splitext(filepath)[1].lower()
    return ext in MIME_TYPES
