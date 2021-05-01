from sqlalchemy import Boolean, Column, Integer, ForeignKey, String
from sqlalchemy.sql import expression

from .base import Base


class User(Base):
    __tablename__ = "users"
    __mapper_args__ = {"eager_defaults": True}

    id = Column(Integer, primary_key=True, index=True, unique=True)
    is_superuser = Column(Boolean, server_default=expression.false())
    username = Column(String, index=True, unique=True)
    password = Column(String)


class UserRelatedMixin:
    user_id = Column(
        Integer,
        ForeignKey(f"{User.__tablename__}.id", ondelete="CASCADE", onupdate="CASCADE"),
        nullable=False,
    )
