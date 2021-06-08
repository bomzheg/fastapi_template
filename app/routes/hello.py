from fastapi import Request, FastAPI


async def hello(request: Request, foo: int = 0):

    return {"message": f"Hello, {request.state.worker.name}  {foo}"}


def setup_hello(app: FastAPI):
    app.router.add_api_route("/hello", hello)
