from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from strawberry.fastapi import GraphQLRouter
from schema import schema

app = FastAPI(title="GraphQL API with Strawberry")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Connect Strawberry schema to FastAPI using the GraphQLRouter
graphql_app = GraphQLRouter(schema)

# Attach it to the '/graphql' endpoint. It will also serve an interactive GraphiQL GUI!
app.include_router(graphql_app, prefix="/graphql")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
