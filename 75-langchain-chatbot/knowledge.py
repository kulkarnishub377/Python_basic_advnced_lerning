import os
from config import CHUNK_SIZE, CHUNK_OVERLAP


def load_knowledge_base(directory: str = "data") -> list:
    """Load all .txt files from the data directory."""
    documents = []
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            filepath = os.path.join(directory, filename)
            with open(filepath, "r", encoding="utf-8") as f:
                documents.append({"content": f.read(), "source": filename})
    return documents


def split_into_chunks(documents: list) -> list:
    """Split documents into overlapping chunks for better retrieval."""
    chunks = []
    for doc in documents:
        text = doc["content"]
        source = doc["source"]
        start = 0
        chunk_idx = 0
        while start < len(text):
            end = start + CHUNK_SIZE
            chunk_text = text[start:end]
            chunks.append({
                "text": chunk_text.strip(),
                "source": f"{source}:chunk_{chunk_idx}",
            })
            start += CHUNK_SIZE - CHUNK_OVERLAP
            chunk_idx += 1
    return chunks


def get_knowledge_chunks() -> list:
    """Main entry point: load and split the knowledge base."""
    docs = load_knowledge_base()
    chunks = split_into_chunks(docs)
    return chunks
