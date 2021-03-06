import logging.config
from pathlib import Path

import yaml


logger = logging.getLogger(__name__)


def setup_logging(app_dir: Path, config_path: Path):
    log_dir = app_dir / "log"
    log_dir.mkdir(exist_ok=True)
    with (config_path / "logging.yaml").open("r") as f:
        logging_config = yaml.safe_load(f)
        logging.config.dictConfig(logging_config)
    logger.info("Logging configured successfully")
