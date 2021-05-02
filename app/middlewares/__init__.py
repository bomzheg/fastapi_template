from fastapi import FastAPI
from sqlalchemy.orm import sessionmaker
from starlette.middleware.base import BaseHTTPMiddleware

from app.middlewares.acl_middleware import check_login
from app.middlewares.db_middleware import DatabaseMiddleware


def setup_middlewares(app: FastAPI, pool: sessionmaker):
    app.add_middleware(BaseHTTPMiddleware, dispatch=check_login)
    app.add_middleware(BaseHTTPMiddleware, dispatch=DatabaseMiddleware(pool=pool))

