# 74 - gRPC Python Microservice

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Difficulty: Expert](https://img.shields.io/badge/Difficulty-Expert-red?style=for-the-badge)
![gRPC](https://img.shields.io/badge/gRPC-244c5a?style=for-the-badge&logo=google&logoColor=white)

## What It Does

Implements a high-performance **gRPC** (Google Remote Procedure Call) microservice using Protocol Buffers for binary serialization. Unlike standard JSON-based REST APIs, gRPC uses a strict `.proto` schema to generate Python stubs, resulting in type-safe, significantly faster inter-service communication. Includes a REST-to-gRPC proxy so the browser frontend can compare performance.

## Project Structure

```text
74-grpc-service/
  protos/
    product.proto     # Protocol Buffers schema definition
  server.py           # gRPC server implementing the service
  client.py           # Python gRPC client for testing
  proxy.py            # FastAPI REST proxy translating HTTP to gRPC calls
  codegen.py          # Script to compile .proto into Python stubs
  config.py           # Server addresses and port constants
  requirements.txt    # Dependencies
  index.html          # Unified frontend comparing REST vs gRPC speed
  README.md           # This file
```

## Setup and Run

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Generate Python stubs from .proto
```bash
python codegen.py
```

### 3. Start the gRPC Server (Terminal 1)
```bash
python server.py
```

### 4. Start the REST Proxy (Terminal 2)
```bash
uvicorn proxy:app --reload --port 8000
```

### 5. Test with the Python client
```bash
python client.py
```

### 6. Open the Frontend
Open `index.html` in your browser for a speed comparison dashboard.

## Example Output

```text
# Python gRPC Client
$ python client.py
[Client] Connected to gRPC server at localhost:50051
[Client] CreateProduct(name='Laptop', price=999.99) -> id=1
[Client] GetProduct(id=1) -> Product(id=1, name='Laptop', price=999.99, in_stock=True)
[Client] ListProducts() -> 3 products found
[Client] 100 gRPC round-trips completed in 0.34 seconds (avg 3.4ms/call)

# REST Proxy comparison
$ curl http://localhost:8000/products
[{"id":1,"name":"Laptop","price":999.99,"in_stock":true}]
```

## Core Concepts

- **Protocol Buffers**: Language-neutral binary serialization format (smaller and faster than JSON).
- **Service Definition**: The `.proto` file defines RPC methods like a contract between client and server.
- **Code Generation**: `grpcio-tools` compiles `.proto` into Python classes automatically.
- **Streaming**: gRPC natively supports unary, server-streaming, client-streaming, and bidirectional streaming.
- **REST Proxy**: A FastAPI layer that translates browser HTTP requests into gRPC calls.
