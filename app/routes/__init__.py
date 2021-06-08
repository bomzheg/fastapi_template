from fastapi import FastAPI

from .hello import setup_hello


def setup_routes(app: FastAPI):
    setup_hello(app)
