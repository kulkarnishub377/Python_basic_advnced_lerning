# 75 - Generative AI Chatbot (LangChain)

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Difficulty: Expert](https://img.shields.io/badge/Difficulty-Expert-red?style=for-the-badge)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-121212?style=for-the-badge)

## What It Does

Builds an AI-powered question-answering chatbot using the **LangChain** framework. The bot uses a Retrieval-Augmented Generation (RAG) pattern: it loads a knowledge base of text documents, splits them into chunks, stores them in a vector database (FAISS), and retrieves the most relevant context before generating an answer. Includes a ChatGPT-style frontend.

## Project Structure

```text
75-langchain-chatbot/
  main.py            # FastAPI entry point with chat endpoint
  bot.py             # LangChain chain construction (retriever + LLM)
  knowledge.py       # Knowledge base loader and text splitter
  config.py          # LLM model config and API key placeholder
  data/
    knowledge_base.txt  # Mock knowledge documents
  requirements.txt   # Dependencies
  index.html         # Unified ChatGPT-style frontend
  README.md          # This file
```

## Setup and Run

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Configure your API key
Edit `config.py` and set your OpenAI API key (or use a local model).

### 3. Start the server
```bash
uvicorn main:app --reload
```

### 4. Open the Frontend
Open `index.html` in your browser to start chatting.

## Example Output

```json
// POST /chat  {"question": "What is Python used for?"}
{
  "question": "What is Python used for?",
  "answer": "Python is a versatile programming language used for web development, data science, machine learning, automation, scripting, and building APIs. It is known for its readability and large ecosystem of libraries.",
  "sources": ["knowledge_base.txt:chunk_3", "knowledge_base.txt:chunk_7"],
  "response_time_ms": 1250
}
```

## Core Concepts

- **RAG (Retrieval-Augmented Generation)**: Combines document retrieval with LLM generation for grounded answers.
- **Text Splitting**: Large documents are chunked into overlapping segments for better retrieval.
- **Vector Store (FAISS)**: Embeds text chunks into vectors for semantic similarity search.
- **Prompt Templates**: LangChain's `PromptTemplate` structures the LLM input with context injection.
- **Conversation Memory**: `ConversationBufferMemory` maintains chat history across turns.
