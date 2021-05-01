import logging
from pathlib import Path

from dotenv import load_dotenv

from app.config.db import load_db_config
from app.config.logging_config import setup_logging
from app.models.config import Config


logger = logging.getLogger(__name__)


def load_config(app_dir: Path = Path(__file__).parent.parent.parent) -> Config:
    config_path = app_dir / "config"
    load_dotenv(config_path / ".env")
    setup_logging(app_dir, config_path)
    return Config(
        app_dir=app_dir,
        db=load_db_config(config_path),
    )
