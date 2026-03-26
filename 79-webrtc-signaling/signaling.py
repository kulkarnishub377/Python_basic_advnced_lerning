from fastapi import WebSocket
import uuid


class Room:
    """A signaling room holding up to 2 peers for a P2P connection."""

    def __init__(self, name: str):
        self.name = name
        self.peers: dict[str, WebSocket] = {}

    async def add_peer(self, ws: WebSocket) -> str:
        peer_id = str(uuid.uuid4())[:8]
        self.peers[peer_id] = ws
        print(f'[Signaling] Peer "{peer_id}" joined room "{self.name}"')
        return peer_id

    def remove_peer(self, peer_id: str):
        self.peers.pop(peer_id, None)
        print(f'[Signaling] Peer "{peer_id}" left room "{self.name}"')

    async def relay(self, sender_id: str, message: dict):
        """Forward a message to all OTHER peers in the room."""
        for pid, ws in self.peers.items():
            if pid != sender_id:
                try:
                    await ws.send_json(message)
                except Exception:
                    pass


# Global room registry
rooms: dict[str, Room] = {}


def get_or_create_room(name: str) -> Room:
    if name not in rooms:
        rooms[name] = Room(name)
    return rooms[name]
