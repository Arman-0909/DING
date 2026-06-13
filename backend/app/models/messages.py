from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey
from sqlalchemy import DateTime
from datetime import datetime
from app.db.base import Base
from sqlalchemy import DateTime
from datetime import datetime


created_at = Column(
    DateTime,
    default=datetime.utcnow
)

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

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )