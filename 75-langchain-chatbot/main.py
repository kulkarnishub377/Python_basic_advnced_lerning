import time
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from bot import generate_answer

app = FastAPI(title="LangChain RAG Chatbot API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class ChatRequest(BaseModel):
    question: str


@app.post("/chat")
def chat(req: ChatRequest):
    """Send a question and receive a RAG-based answer from the knowledge base."""
    start = time.perf_counter()
    result = generate_answer(req.question)
    elapsed = round((time.perf_counter() - start) * 1000, 1)

    return {
        "question": req.question,
        "answer": result["answer"],
        "sources": result["sources"],
        "response_time_ms": elapsed,
    }


@app.get("/health")
def health():
    return {"status": "ok", "service": "langchain-chatbot"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
