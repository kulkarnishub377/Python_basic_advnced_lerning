# 56 - Real-Time WebSocket Chat Application

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Difficulty: Expert](https://img.shields.io/badge/Difficulty-Expert-red?style=for-the-badge)
![Phase](https://img.shields.io/badge/Phase-7_Expert_Projects-blue?style=for-the-badge)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)

## What It Does

A real-time chat room where multiple clients can connect via WebSockets and exchange messages instantly without HTTP polling. It features a FastAPI backend managing active WebSocket connections and broadcasting messages, along with a sleek, modern Vanilla HTML/CSS/JS frontend interface.

## Project Structure

```text
56-websocket-chat/
  main.py              # FastAPI server managing WebSocket connections
  requirements.txt     # Python dependencies
  frontend/
    index.html         # Chat UI structure
    style.css          # Modern chat interface styling
    app.js             # WebSocket client logic
  README.md            # This file
```

## Setup and Run

### 1. Backend Setup

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

### 2. Frontend Setup

Simply open `frontend/index.html` in your web browser. You can open multiple tabs or multiple browsers to see the real-time chat in action!

## Core Concepts

- **WebSockets protocol (`ws://`)** for full-duplex communication
- `fastapi.WebSocket` and `await websocket.accept()`
- Connection Manager pattern to track active clients
- Broadcasting messages to all connected clients
- Handling client disconnects gracefully (`WebSocketDisconnect`)
- Vanilla JS `WebSocket` API on the frontend

## What You Will Learn

You will learn how to break away from standard HTTP request/response cycles to build truly real-time applications. You'll understand how to manage persistent state (active connections) in a web framework, and how to synchronize state across multiple separate frontend clients instantly.

## Example Output

```text
Server log:
INFO:     Uvicorn running on http://127.0.0.1:8000
INFO:     connection open
INFO:     Client #1 connected
INFO:     Client #2 connected
INFO:     Broadcasting message from Client 1...
INFO:     Client #2 disconnected
```
