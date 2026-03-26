# 67 - GraphQL API with Strawberry

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Difficulty: Expert](https://img.shields.io/badge/Difficulty-Expert-red?style=for-the-badge)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![GraphQL](https://img.shields.io/badge/GraphQL-E10098?style=for-the-badge&logo=graphql&logoColor=white)

## What It Does

This project integrates **GraphQL** into a FastAPI application using the `strawberry` library. Unlike REST, where the server dictates the JSON response shape, GraphQL allows the client to request *exactly* the fields it wants. The project features a unified HTML/JS frontend that sends dynamic GraphQL string queries and mutations to the backend.

## Project Structure

```text
67-fastapi-graphql/
  main.py            # FastAPI Entry point & GraphQL Router setup
  schema.py          # Strawberry GraphQL type definitions
  resolvers.py       # Functions that fetch or modify data for fields
  index.html         # Unified single-file Frontend dashboard
  requirements.txt   # Dependencies
  README.md          # This file
```

## Setup and Run

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Start the FastAPI Server

```bash
uvicorn main:app --reload
```

### 3. Open the Frontend
Open `index.html` directly in your browser. Alternatively, navigate to `http://127.0.0.1:8000/graphql` to use Strawberry's built-in interactive GraphiQL explorer.



## Example Output

```graphql
# Query Sent
{ authors { name, books { title } } }

# JSON Response Received
{
  "data": {
    "authors": [
      {
        "name": "George Orwell",
        "books": [{ "title": "1984" }, { "title": "Animal Farm" }]
      }
    ]
  }
}
```
## Core Concepts

- **Queries (`Query`)**: Equivalent to HTTP GET in REST. Used for fetching data.
- **Mutations (`Mutation`)**: Equivalent to HTTP POST/PUT/DELETE. Used for modifying data.
- **Resolvers**: Python functions decorated with `@strawberry.field` that tell GraphQL *how* to fetch the data for a specific field.
- **Overfetching/Underfetching elimination**: The client specifies a string like `{ users { name } }` to only retrieve names instead of the entire user object.
