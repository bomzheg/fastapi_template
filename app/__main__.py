import logging
from pathlib import Path

import uvicorn
from fastapi import FastAPI

from app.config import load_config
from app.config.logging_config import setup_logging
from app.middlewares import setup_middlewares
from app.models.db.base import create_pool
from app.routes import setup_routes


app_dir = Path(__file__).parent.parent
logger = logging.getLogger(__name__)


def main() -> FastAPI:
    config = load_config(app_dir)
    pool = create_pool(config.db)

    logger.info("started")

    app = FastAPI()
    setup_middlewares(app, pool)
    setup_routes(app)
    return app


if __name__ == '__main__':
    setup_logging(app_dir, app_dir / "config")
    uvicorn.run(
        'app:main',
        factory=True,
        log_config=None
    )
