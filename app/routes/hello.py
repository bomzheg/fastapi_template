from fastapi import Request


async def hello(request: Request, foo: int = 0):

    return {"message": f"Hello, {request.state.worker.name}  {foo}"}
