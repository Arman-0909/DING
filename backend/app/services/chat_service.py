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
    db.refresh(member)

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


def add_member(
    db: Session,
    chat_id: int,
    user_id: int
):
    existing = (
        db.query(ChatMember)
        .filter(
            ChatMember.chat_id == chat_id,
            ChatMember.user_id == user_id
        )
        .first()
    )

    if existing:
        return existing

    member = ChatMember(
        chat_id=chat_id,
        user_id=user_id
    )

    db.add(member)
    db.commit()
    db.refresh(member)

    return member


def get_chat_members(
    db: Session,
    chat_id: int
):
    return (
        db.query(ChatMember)
        .filter(
            ChatMember.chat_id == chat_id
        )
        .all()
    )


def is_chat_member(
    db: Session,
    chat_id: int,
    user_id: int
):
    return (
        db.query(ChatMember)
        .filter(
            ChatMember.chat_id == chat_id,
            ChatMember.user_id == user_id
        )
        .first()
    )


def remove_member(
    db: Session,
    chat_id: int,
    user_id: int
):
    member = (
        db.query(ChatMember)
        .filter(
            ChatMember.chat_id == chat_id,
            ChatMember.user_id == user_id
        )
        .first()
    )

    if not member:
        return False

    db.delete(member)
    db.commit()

    return True