from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Boolean

from app.db.base import Base


class Chat(Base):
    __tablename__ = "chats"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    name = Column(
        String,
        nullable=True
    )

    is_group = Column(
        Boolean,
        default=False
    )