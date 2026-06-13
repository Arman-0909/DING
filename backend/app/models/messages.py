from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey

from app.db.base import Base


class Message(Base):
    __tablename__ = "messages"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    chat_id = Column(
        Integer,
        ForeignKey("chats.id")
    )

    sender_id = Column(
        Integer,
        ForeignKey("users.id")
    )

    content = Column(
        String
    )