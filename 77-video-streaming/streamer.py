from config import CHUNK_SIZE


def range_reader(filepath: str, start: int, end: int):
    """Generator that yields file chunks within the requested byte range."""
    with open(filepath, "rb") as f:
        f.seek(start)
        remaining = end - start + 1
        while remaining > 0:
            chunk_size = min(CHUNK_SIZE, remaining)
            data = f.read(chunk_size)
            if not data:
                break
            remaining -= len(data)
            yield data


def parse_range_header(range_header: str, file_size: int) -> tuple:
    """Parse the HTTP Range header and return (start, end) byte positions."""
    try:
        range_spec = range_header.replace("bytes=", "")
        parts = range_spec.split("-")
        start = int(parts[0]) if parts[0] else 0
        end = int(parts[1]) if parts[1] else file_size - 1
        end = min(end, file_size - 1)
        return start, end
    except (ValueError, IndexError):
        return 0, file_size - 1
