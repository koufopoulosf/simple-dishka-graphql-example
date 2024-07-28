from dishka.integrations.fastapi import setup_dishka
from fastapi import FastAPI

from app_provider import container
from api_graphql_context import graphql_app

app = FastAPI()

setup_dishka(container, app)

app.include_router(graphql_app, prefix="/graphql")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)