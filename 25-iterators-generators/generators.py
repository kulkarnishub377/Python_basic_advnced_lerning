import sys
import tracemalloc

def read_large_file(path):
    """
    A pure Generator Function inherently utilizing `yield`!
    This physically isolates lines seamlessly parsing strictly exactly one 
    element sequentially safely avoiding totally loading structural arrays!
    """
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            # Yield pauses the function strictly, returning a dynamically active variable natively!
            yield line.strip()

def filter_lines(lines, keyword):
    """
    A fundamentally advanced Generator Expression Pipeline!
    `(l for l in lines if ...)` constructs a generator strictly from a generator!
    """
    return (l for l in lines if keyword in l)

def infinite_counter(start=0):
    """
    Because generators inherently pause cleanly natively, you absolutely can construct 
    completely infinite computational loops processing mathematical values indefinitely securely!
    """
    current = start
    while True:
        yield current
        current += 1
