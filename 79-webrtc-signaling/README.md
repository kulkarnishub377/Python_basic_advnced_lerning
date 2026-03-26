# 79 - WebRTC P2P Signaling Server

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Difficulty: Expert](https://img.shields.io/badge/Difficulty-Expert-red?style=for-the-badge)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![WebRTC](https://img.shields.io/badge/WebRTC-333333?style=for-the-badge&logo=webrtc&logoColor=white)

## What It Does

Implements a **WebRTC signaling server** using FastAPI WebSockets. The Python server does NOT relay media data. Instead, it acts as a matchmaker: when two browser peers connect, the server exchanges their SDP (Session Description Protocol) offers/answers and ICE candidates so they can establish a direct peer-to-peer connection for video/audio without any server in between.

## Project Structure

```text
79-webrtc-signaling/
  main.py            # FastAPI entry point with WebSocket signaling
  signaling.py       # Room manager and peer connection state tracking
  models.py          # Pydantic schemas for signaling messages
  config.py          # ICE server config, signaling port
  requirements.txt   # Dependencies
  index.html         # Unified dual-panel video chat frontend
  README.md          # This file
```

## Setup and Run

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Start the signaling server
```bash
uvicorn main:app --reload --port 8000
```

### 3. Open TWO browser tabs
Open `index.html` in two separate tabs (or two different browsers). Both will connect to the signaling server, exchange SDP, and establish a direct P2P video stream.

## Example Output

```text
# Server terminal
[Signaling] Peer "abc123" joined room "default"
[Signaling] Peer "def456" joined room "default"
[Signaling] Forwarding SDP offer from abc123 -> def456
[Signaling] Forwarding SDP answer from def456 -> abc123
[Signaling] Exchanging ICE candidates...
[Signaling] P2P connection established! Server is no longer in the data path.

# Browser Console (Peer A)
WebSocket connected to signaling server
Sending SDP offer...
Received SDP answer from remote peer
ICE connection state: connected
Video stream active - direct P2P!
```

## Core Concepts

- **Signaling Server**: Exchanges metadata (SDP, ICE) but never touches the actual media stream.
- **SDP (Session Description Protocol)**: Describes the media capabilities (codecs, resolution) of each peer.
- **ICE Candidates**: Network path options (STUN/TURN) for finding the optimal P2P route.
- **Peer-to-Peer**: After the handshake, data flows directly between browsers with zero server involvement.
