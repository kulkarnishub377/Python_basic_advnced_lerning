from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from typing import List
import json
import logging

# Configure basic logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title="WebSocket Chat Server")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class ConnectionManager:
    """Manages active websocket connections and broadcasts messages."""
    def __init__(self):
        self.active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)
        logger.info(f"Client connected. Total clients: {len(self.active_connections)}")

    def disconnect(self, websocket: WebSocket):
        if websocket in self.active_connections:
            self.active_connections.remove(websocket)
            logger.info(f"Client disconnected. Total clients: {len(self.active_connections)}")

    async def broadcast(self, message: str):
        """Send a message to all connected clients."""
        for connection in self.active_connections:
            try:
                await connection.send_text(message)
            except Exception as e:
                logger.error(f"Error sending message to client: {e}")


# Initialize the connection manager
manager = ConnectionManager()


@app.websocket("/ws/chat/{client_id}")
async def websocket_endpoint(websocket: WebSocket, client_id: str):
    """
    WebSocket endpoint for the chat room.
    Accepts the connection, listens for messages, and broadcasts them.
    """
    await manager.connect(websocket)
    
    # Announce new user
    join_msg = json.dumps({"type": "system", "content": f"User {client_id} joined the chat"})
    await manager.broadcast(join_msg)
    
    try:
        while True:
            # Wait for any message from the client
            data = await websocket.receive_text()
            
            # Format the message as JSON
            message = json.dumps({
                "type": "chat",
                "client_id": client_id,
                "content": data
            })
            
            # Broadcast the message to everyone (including the sender)
            await manager.broadcast(message)
            
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        # Announce user left
        leave_msg = json.dumps({"type": "system", "content": f"User {client_id} left the chat"})
        await manager.broadcast(leave_msg)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
