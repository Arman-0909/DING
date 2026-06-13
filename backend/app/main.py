from fastapi import FastAPI

from app.api.auth import router as auth_router
from app.db.base import Base
from app.db.database import engine
from app.models.users import User
from app.models.chats import Chat
from app.models.chat_members import ChatMember
from app.models.messages import Message
from app.api.chats import router as chats_router


Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="DING API"
)

app.include_router(
    auth_router
)

app.include_router(
    chats_router
)