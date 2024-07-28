from strawberry.types import Info
import strawberry

from api_graphql_type import HelloResponse
from hello_provider import HelloWorld

@strawberry.type
class Mutation:
    @strawberry.mutation
    async def say_hello(self, name: str, info: Info) -> HelloResponse:
        hello_world = await info.context.get_hello_world()
        message = hello_world.say_hello(name)
        return HelloResponse(message=message)