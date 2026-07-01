from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from app.db.database import get_db

from app.models.users import User

from app.core.security import get_current_user

from app.schemas.chats import (
    ChatCreate,
    ChatResponse
)

from app.schemas.chat_members import (
    AddMember
)

from app.services.chat_service import (
    create_chat,
    get_user_chats,
    add_member,
    get_chat_members,
    is_chat_member
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


@router.post(
    "/{chat_id}/members"
)
def add_chat_member(
    chat_id: int,
    member: AddMember,
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

    if is_chat_member(
        db,
        chat_id,
        member.user_id
    ):
        raise HTTPException(
            status_code=409,
            detail="Member already exists in the chat"
        )

    add_member(
        db,
        chat_id,
        member.user_id
    )

    return {
        "message": "Member added"
    }


@router.get(
    "/{chat_id}/members"
)
def get_members(
    chat_id: int,
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

    return get_chat_members(
        db,
        chat_id
    )