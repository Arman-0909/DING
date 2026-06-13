from fastapi import FastAPI

from app.api.auth import router as auth_router
from app.db.base import Base
from app.db.database import engine

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="DING API"
)

app.include_router(
    auth_router
)