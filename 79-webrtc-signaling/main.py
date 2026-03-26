import json
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from signaling import get_or_create_room
from config import ICE_SERVERS

app = FastAPI(title="WebRTC Signaling Server")

app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])


@app.websocket("/ws/{room_name}")
async def websocket_signaling(websocket: WebSocket, room_name: str = "default"):
    """
    WebSocket endpoint for WebRTC signaling.
    Peers join a room. The server relays SDP offers/answers and ICE candidates
    between peers so they can establish a direct P2P connection.
    """
    await websocket.accept()
    room = get_or_create_room(room_name)
    peer_id = await room.add_peer(websocket)

    # Send the peer their ID and ICE server config
    await websocket.send_json({
        "type": "welcome",
        "peer_id": peer_id,
        "ice_servers": ICE_SERVERS,
        "peers_in_room": len(room.peers),
    })

    # Notify others that a new peer joined
    await room.relay(peer_id, {"type": "peer_joined", "peer_id": peer_id})

    try:
        while True:
            raw = await websocket.receive_text()
            data = json.loads(raw)
            data["sender_id"] = peer_id

            msg_type = data.get("type", "")
            if msg_type in ("offer", "answer", "candidate"):
                print(f"[Signaling] Relaying {msg_type} from {peer_id}")
                await room.relay(peer_id, data)
    except WebSocketDisconnect:
        room.remove_peer(peer_id)
        await room.relay(peer_id, {"type": "peer_left", "peer_id": peer_id})


@app.get("/health")
def health():
    return {"status": "ok", "service": "webrtc-signaling"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
