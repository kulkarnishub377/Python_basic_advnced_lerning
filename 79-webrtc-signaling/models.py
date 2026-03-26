from pydantic import BaseModel
from typing import Optional


class SignalMessage(BaseModel):
    type: str                   # "offer", "answer", "candidate", "join", "leave"
    room: str = "default"
    sender_id: Optional[str] = None
    sdp: Optional[str] = None   # For offer/answer
    candidate: Optional[dict] = None  # For ICE candidates
