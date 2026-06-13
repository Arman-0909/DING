from sqlalchemy.orm import Session

from app.models.chats import Chat
from app.models.chat_members import ChatMember


def create_chat(
    db: Session,
    user_id: int,
    name: str | None,
    is_group: bool
):
    chat = Chat(
        name=name,
        is_group=is_group
    )

    db.add(chat)
    db.commit()
    db.refresh(chat)

    member = ChatMember(
        chat_id=chat.id,
        user_id=user_id
    )

    db.add(member)
    db.commit()

    return chat


def get_user_chats(
    db: Session,
    user_id: int
):
    return (
        db.query(Chat)
        .join(
            ChatMember,
            Chat.id == ChatMember.chat_id
        )
        .filter(
            ChatMember.user_id == user_id
        )
        .all()
    )