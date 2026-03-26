# 73 - Apache Kafka Event Streaming

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Difficulty: Expert](https://img.shields.io/badge/Difficulty-Expert-red?style=for-the-badge)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Kafka](https://img.shields.io/badge/Kafka-231F20?style=for-the-badge&logo=apachekafka&logoColor=white)

## What It Does

Demonstrates a real-time **distributed event streaming** architecture. A Producer script generates thousands of analytics events (page views, clicks, purchases) and publishes them to a Kafka topic. A Consumer script reads from the topic in real-time and aggregates the data. A FastAPI layer exposes the aggregated metrics, and a unified frontend dashboard polls and visualizes the live counts.

## Project Structure

```text
73-kafka-streaming/
  producer.py        # Publishes analytics events to Kafka topic
  consumer.py        # Reads events from Kafka and aggregates metrics
  aggregator.py      # In-memory metrics store shared with the API
  api.py             # FastAPI endpoints exposing aggregated data
  config.py          # Kafka broker URL, topic name constants
  schemas.py         # Pydantic models for events
  requirements.txt   # Dependencies
  index.html         # Unified real-time metrics dashboard
  README.md          # This file
```

## Setup and Run

### Prerequisites
- Apache Kafka running locally on port 9092

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Start the Consumer (Terminal 1)
```bash
python consumer.py
```

### 3. Start the API Server (Terminal 2)
```bash
uvicorn api:app --reload --port 8000
```

### 4. Start the Producer (Terminal 3)
```bash
python producer.py
```

### 5. Open the Frontend
Open `index.html` in your browser to watch real-time metrics being updated.

## Example Output

```text
# Producer terminal
[Producer] Sent: {"event_type": "page_view", "page": "/home", "user_id": 42, "timestamp": "2024-01-15T10:30:00"}
[Producer] Sent: {"event_type": "click", "element": "buy_button", "user_id": 17, "timestamp": "2024-01-15T10:30:01"}
[Producer] Sent: {"event_type": "purchase", "product": "Laptop", "amount": 999.99, "timestamp": "2024-01-15T10:30:02"}
[Producer] 1000 events published in 3.2 seconds

# Consumer terminal
[Consumer] Consumed: page_view | Total page_views: 487
[Consumer] Consumed: click | Total clicks: 312
[Consumer] Consumed: purchase | Total purchases: 201

# API Response: GET /metrics
{
  "page_views": 487,
  "clicks": 312,
  "purchases": 201,
  "total_revenue": 45230.50,
  "events_per_second": 312.5
}
```

## Core Concepts

- **Producer/Consumer Pattern**: Decoupled services communicate via a message broker.
- **Topics & Partitions**: Kafka organizes messages into topics for parallel consumption.
- **At-Least-Once Delivery**: Kafka guarantees every message is delivered at least once.
- **Real-Time Aggregation**: Consumer processes events as they arrive, maintaining running totals.
- **Backpressure Handling**: Producer and consumer operate at independent speeds.
