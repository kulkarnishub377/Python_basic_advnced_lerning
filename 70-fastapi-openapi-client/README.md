# 70 - OpenAPI Client Generator

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Difficulty: Expert](https://img.shields.io/badge/Difficulty-Expert-red?style=for-the-badge)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)

## What It Does

FastAPI automatically generates a comprehensive `openapi.json` specification of all your routes, schemas, and parameters based on Pydantic typings. This project demonstrates how you can programmatically hit that `/openapi.json` endpoint and parse the schema to automatically generate a fully-typed Python Client SDK (wrapper) so that other frontend teams or microservices don't have to write HTTP requests manually.

It includes a code generator script that writes the `client.py` file to disk automatically.

## Project Structure

```text
70-fastapi-openapi-client/
  main.py                # FastAPI Server with various Typed Endpoints
  generate_client.py     # Script that fetches openapi.json & writes the SDK
  tests/
    test_client.py       # A test using the newly generated SDK
  index.html             # A web UI visualizing the generated output
  requirements.txt       # Dependencies
  README.md              # This file
```

## Setup and Run

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Start the FastAPI Server (Terminal 1)

```bash
uvicorn main:app --reload
```

### 3. Generate the Client SDK (Terminal 2)

While the server is running, execute the generator script:
```bash
python generate_client.py
```
*You will notice a new file `client.py` created in the root directory containing fully typed Python wrapper methods.*

### 4. Test the generated Client (Terminal 2)
```bash
python tests/test_client.py
```



## Example Output

```text
$ python generate_client.py
[*] Fetching OpenAPI schema from http://127.0.0.1:8000/openapi.json...
[*] Parsing paths and generating code...
[+] Successfully generated Python SDK at client.py!

$ python tests/test_client.py
--- Testing Auto-Generated API Client ---

[*] Creating a new product...
Created: {'id': 1, 'name': 'Mechanical Keyboard', 'price': 129.99, 'description': 'Clicky switches'}

[*] Fetching all products...
Products: [{'id': 1, 'name': 'Mechanical Keyboard', 'price': 129.99, 'description': 'Clicky switches'}]
```
## Core Concepts

- **Schema Introspection**: `app.openapi()` returns the entire OpenAPI JSON mapping.
- **Code Generation (Codegen)**: Parsing a JSON schema loop to dynamically output source code syntax (`.py` files) into strings and saving them to disk.
- **SDK Wrapping**: Generating a class (`ApiClient`) that internally handles `httpx` and abstracts away the URLs and `requests.get()` code.
