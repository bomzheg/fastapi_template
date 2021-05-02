from dataclasses import dataclass
from pathlib import Path

from .db import DBConfig


@dataclass
class Config:
    app_dir: Path
    db: DBConfig
    secret_key: str
