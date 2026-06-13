from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.db.database import get_db

from app.models.users import User

from app.core.security import get_current_user

from app.schemas.chats import (
    ChatCreate,
    ChatResponse
)

from app.services.chat_service import (
    create_chat,
    get_user_chats
)

router = APIRouter(
    prefix="/chats",
    tags=["Chats"]
)


@router.post(
    "",
    response_model=ChatResponse
)
def create_new_chat(
    chat: ChatCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(
        get_current_user
    )
):
    return create_chat(
        db=db,
        user_id=current_user.id,
        name=chat.name,
        is_group=chat.is_group
    )


@router.get(
    "",
    response_model=list[ChatResponse]
)
def get_chats(
    db: Session = Depends(get_db),
    current_user: User = Depends(
        get_current_user
    )
):
    return get_user_chats(
        db,
        current_user.id
    )