from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.db.database import get_db

from app.core.security import get_current_user

from app.core.security import (
    get_current_user
)

from app.models.users import User

from app.schemas.users import (
    UserCreate,
    UserResponse
)

from app.services.user_service import (
    create_user
)

from fastapi import HTTPException

from app.schemas.auth import (
    LoginRequest,
    TokenResponse
)

from app.services.user_service import (
    get_user_by_email
)

from app.utils.password import (
    verify_password
)

from app.utils.token import (
    create_access_token
)

router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)


@router.get(
    "/me",
    response_model=UserResponse
)
def me(
    current_user: User = Depends(
        get_current_user
    )
):

    return current_user

@router.post(
    "/register",
    response_model=UserResponse
)
def register(
    user: UserCreate,
    db: Session = Depends(get_db)
):
    return create_user(
        db,
        user
    )


@router.post(
    "/login",
    response_model=TokenResponse
)
def login(
    credentials: LoginRequest,
    db: Session = Depends(get_db)
):

    user = get_user_by_email(
        db,
        credentials.email
    )

    if not user:
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )

    if not verify_password(
        credentials.password,
        user.password_hash
    ):
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )

    token = create_access_token(
        {
            "sub": str(user.id)
        }
    )

    return {
        "access_token": token,
        "token_type": "bearer"
    }