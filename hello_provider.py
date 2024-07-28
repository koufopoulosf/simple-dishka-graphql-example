from dishka import Provider, Scope, provide

class HelloWorld:
    def say_hello(self, name: str) -> str:
        return f"Hello, {name}!"

class HelloProvider(Provider):
    component = "hello"

    @provide(scope=Scope.REQUEST)
    async def get_hello_world(self) -> HelloWorld:
        return HelloWorld()