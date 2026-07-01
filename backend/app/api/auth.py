from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import Request

from sqlalchemy.orm import Session

from app.core.oauth import oauth
from app.core.security import get_current_user

from app.db.database import get_db

from app.models.users import User

from app.schemas.auth import (
    LoginRequest,
    TokenResponse
)

from app.schemas.users import (
    UserCreate,
    UserResponse
)

from app.services.user_service import (
    build_token_response,
    create_user,
    generate_google_username,
    get_user_by_email,
    get_user_by_google_id,
    get_user_by_username,
    update_google_account
)

from app.utils.password import verify_password
from app.utils.token import create_access_token


router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)


@router.get(
    "/me",
    response_model=UserResponse
)
def me(
    current_user: User = Depends(get_current_user)
):
    return current_user


@router.post(
    "/register",
    response_model=UserResponse,
    status_code=201
)
def register(
    user: UserCreate,
    db: Session = Depends(get_db)
):

    if get_user_by_email(
        db,
        user.email
    ):
        raise HTTPException(
            status_code=409,
            detail="Email already registered."
        )

    if get_user_by_username(
        db,
        user.username
    ):
        raise HTTPException(
            status_code=409,
            detail="Username already taken."
        )

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
            detail="Invalid credentials."
        )

    if user.password_hash is None:
        raise HTTPException(
            status_code=400,
            detail="This account uses Google Sign-In."
        )

    if not verify_password(
        credentials.password,
        user.password_hash
    ):
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials."
        )

    token = create_access_token(
        {
            "sub": str(user.id)
        }
    )

    return build_token_response(
        token,
        user
    )


@router.get("/google/login")
async def google_login(
    request: Request
):

    redirect_uri = request.url_for(
        "google_callback"
    )

    return await oauth.google.authorize_redirect(
        request,
        redirect_uri
    )


@router.get(
    "/google/callback",
    response_model=TokenResponse,
    name="google_callback"
)
async def google_callback(
    request: Request,
    db: Session = Depends(get_db)
):

    token = await oauth.google.authorize_access_token(
        request
    )

    user_info = await oauth.google.userinfo(
        token=token
    )

    google_id = user_info["sub"]
    email = user_info["email"]

    user = get_user_by_google_id(
        db,
        google_id
    )

    if not user:

        user = get_user_by_email(
            db,
            email
        )

        if user:

            user = update_google_account(
                db,
                user,
                google_id
            )

        else:

            username = generate_google_username(
                user_info["name"]
            )

            user = User(
                username=username,
                email=email,
                google_id=google_id,
                auth_provider="google"
            )

            db.add(user)
            db.commit()
            db.refresh(user)

    jwt_token = create_access_token(
        {
            "sub": str(user.id)
        }
    )

    return build_token_response(
        jwt_token,
        user
    )