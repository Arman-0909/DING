from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import Query

from sqlalchemy.orm import Session

from app.db.database import get_db

from app.models.users import User

from app.core.security import get_current_user

from app.schemas.messages import (
    MessageCreate,
    MessageResponse
)

from app.services.message_service import (
    create_message,
    get_chat_messages
)

from app.services.chat_service import (
    is_chat_member
)

router = APIRouter(
    prefix="/messages",
    tags=["Messages"]
)


@router.post(
    "",
    response_model=MessageResponse
)
def send_message(
    message: MessageCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(
        get_current_user
    )
):

    if not is_chat_member(
        db,
        message.chat_id,
        current_user.id
    ):
        raise HTTPException(
            status_code=403,
            detail="Not a chat member"
        )

    return create_message(
        db=db,
        chat_id=message.chat_id,
        sender_id=current_user.id,
        content=message.content
    )


@router.get(
    "/{chat_id}",
    response_model=list[MessageResponse]
)
def get_messages(
    chat_id: int,
    limit: int = Query(
        default=50,
        ge=1,
        le=200
    ),
    offset: int = Query(
        default=0,
        ge=0
    ),
    db: Session = Depends(get_db),
    current_user: User = Depends(
        get_current_user
    )
):

    if not is_chat_member(
        db,
        chat_id,
        current_user.id
    ):
        raise HTTPException(
            status_code=403,
            detail="Not a chat member"
        )

    return get_chat_messages(
        db,
        chat_id,
        limit=limit,
        offset=offset
    )