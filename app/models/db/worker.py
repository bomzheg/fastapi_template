from sqlalchemy import Column, Integer, ForeignKey, String

from .base import Base


class Worker(Base):
    __tablename__ = "workers"
    __mapper_args__ = {"eager_defaults": True}

    id = Column(Integer, primary_key=True, index=True, unique=True)
    token = Column(String, index=True, unique=True, nullable=False)
    name = Column(String, index=True)


class WorkerRelatedMixin:
    worker_id = Column(
        Integer,
        ForeignKey(f"{Worker.__tablename__}.id", ondelete="CASCADE", onupdate="CASCADE"),
        nullable=False,
    )
