import logging
from pathlib import Path

import uvicorn
from fastapi import FastAPI

from app.config import load_config
from app.config.logging_config import setup_logging
from app.routes.hello import hello


app_dir = Path(__file__).parent.parent
logger = logging.getLogger(__name__)


def main() -> FastAPI:
    config = load_config(app_dir)

    logger.info("started")

    app = FastAPI()
    app.get("/hello")(hello)
    return app


if __name__ == '__main__':
    setup_logging(app_dir)
    uvicorn.run(
        'app:main',
        factory=True,
        reload=True,
        log_config=None
    )
