from knowledge import get_knowledge_chunks


def find_relevant_chunks(question: str, top_k: int = 3) -> list:
    """
    Simple keyword-based retrieval (no external LLM dependency).
    In production, you would use FAISS + OpenAI embeddings via LangChain.
    This fallback ensures the project runs without an API key.
    """
    chunks = get_knowledge_chunks()
    question_words = set(question.lower().split())

    scored = []
    for chunk in chunks:
        chunk_words = set(chunk["text"].lower().split())
        overlap = len(question_words & chunk_words)
        scored.append((overlap, chunk))

    scored.sort(key=lambda x: x[0], reverse=True)
    return [c for _, c in scored[:top_k]]


def generate_answer(question: str) -> dict:
    """
    Retrieve relevant chunks and compose an answer.
    Uses keyword matching as a zero-dependency fallback.
    Replace with LangChain's RetrievalQA chain when an LLM API key is available.
    """
    relevant = find_relevant_chunks(question)

    if not relevant:
        return {
            "answer": "I could not find relevant information in my knowledge base.",
            "sources": [],
        }

    # Combine the top chunks as the answer context
    context = " ".join(c["text"] for c in relevant)
    sources = [c["source"] for c in relevant]

    # Trim context to a reasonable answer length
    answer = context[:600]
    if len(context) > 600:
        answer += "..."

    return {
        "answer": answer,
        "sources": sources,
    }
