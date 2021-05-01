from starlette.requests import Request


async def hello(request: Request):
    return {"message": "Hello world"}
