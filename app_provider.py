from dishka import make_async_container

from hello_provider import HelloProvider

container = make_async_container(
    HelloProvider(),
)