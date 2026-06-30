from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Boolean

from app.db.base import Base


class User(Base):
    __tablename__ = "users"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    username = Column(
        String,
        unique=True
    )

    email = Column(
        String,
        unique=True
    )

    password_hash = Column(
    String,
    nullable=True
    )

    google_id = Column(
    String,
    unique=True,
    nullable=True
    )

    auth_provider = Column(
    String,
    default="local"
    )

    is_online = Column(
        Boolean,
        default=False
    )