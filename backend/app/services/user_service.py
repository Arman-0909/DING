from sqlalchemy.orm import Session

from app.models.users import User
from app.schemas.users import UserCreate
from app.utils.password import hash_password


def create_user(
    db: Session,
    user: UserCreate
):
    new_user = User(
        username=user.username,
        email=user.email,
        password_hash=hash_password(
            user.password
        )
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


def get_user_by_email(
    db: Session,
    email: str
):
    return (
        db.query(User)
        .filter(User.email == email)
        .first()
    )