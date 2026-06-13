from fastapi import Depends
from fastapi import HTTPException

from fastapi.security import HTTPBearer
from fastapi.security import HTTPAuthorizationCredentials

from sqlalchemy.orm import Session

from app.db.database import get_db

from app.utils.token import verify_token

from app.services.user_service import (
    get_user_by_id
)

security = HTTPBearer()


def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    db: Session = Depends(get_db)
):

    token = credentials.credentials

    payload = verify_token(token)

    if not payload:
        raise HTTPException(
            status_code=401,
            detail="Invalid token"
        )

    user_id = int(payload["sub"])

    user = get_user_by_id(
        db,
        user_id
    )

    if not user:
        raise HTTPException(
            status_code=401,
            detail="User not found"
        )

    return user