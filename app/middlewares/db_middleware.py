from fastapi import Request, Response
from sqlalchemy.orm import sessionmaker


class DatabaseMiddleware:
    def __init__(self, pool: sessionmaker):
        self.pool = pool

    async def __call__(self, request: Request, call_next) -> Response:
        async with self.pool() as session:
            request.state.session = session
            response = await call_next(request)
        return response
