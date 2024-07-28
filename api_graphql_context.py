from strawberry.fastapi import BaseContext, GraphQLRouter
from dishka import AsyncContainer
from fastapi import Request

from api_graphql_schema import schema
from hello_provider import HelloWorld


class GraphQLContext(BaseContext):
    def __init__(self, request: Request, container: AsyncContainer):
        super().__init__()
        self.request = request
        self.container = container

    async def get_hello_world(self):
        return await self.container.get(HelloWorld, component="hello")

async def get_context(request: Request) -> GraphQLContext:
    return GraphQLContext(request=request, container=request.state.dishka_container)

graphql_app = GraphQLRouter(schema, context_getter=get_context)