from fastapi import Request, Response
from sqlalchemy.future import select
from sqlalchemy.orm import Session

from app.models.db import Worker


async def check_login(request: Request, call_next) -> Response:
    try:
        token = request.headers['Authorization']
    except KeyError:
        return Response(status_code=403)
    session: Session = request.state.session
    result = await session.execute(select(Worker).where(Worker.token == token))
    worker = result.scalars().first()
    if not worker:
        return Response(status_code=403)
    request.state.worker = worker
    return await call_next(request)
