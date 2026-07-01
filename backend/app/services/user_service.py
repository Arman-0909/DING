from sqlalchemy.orm import Session

from app.models.users import User
from app.schemas.users import UserCreate

from app.utils.password import hash_password

import uuid


def create_user(
    db: Session,
    user: UserCreate
):
    new_user = User(
        username=user.username,
        email=user.email,
        password_hash=hash_password(
            user.password
        ),
        auth_provider="local"
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


def get_user_by_id(
    db: Session,
    user_id: int
):
    return (
        db.query(User)
        .filter(User.id == user_id)
        .first()
    )


def get_user_by_email(
    db: Session,
    email: str
):
    return (
        db.query(User)
        .filter(User.email == email)
        .first()
    )


def get_user_by_username(
    db: Session,
    username: str
):
    return (
        db.query(User)
        .filter(User.username == username)
        .first()
    )


def get_user_by_google_id(
    db: Session,
    google_id: str
):
    return (
        db.query(User)
        .filter(User.google_id == google_id)
        .first()
    )


def update_google_account(
    db: Session,
    user: User,
    google_id: str
):
    user.google_id = google_id

    if user.auth_provider == "local":
        user.auth_provider = "local_google"
    elif user.auth_provider != "google":
        user.auth_provider = "google"

    db.commit()
    db.refresh(user)

    return user


def generate_google_username(
    name: str
):
    base = (
        name.strip()
        .lower()
        .replace(" ", "_")
    )

    return (
        f"{base}_{uuid.uuid4().hex[:6]}"
    )


def build_token_response(
    token: str,
    user: User
):
    return {
        "access_token": token,
        "token_type": "bearer",
        "user": {
            "id": user.id,
            "username": user.username,
            "email": user.email
        }
    }