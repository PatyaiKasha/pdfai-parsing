from typing import Generator
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from jose import jwt, JWTError

from app.core.database import SessionLocal
from app.core import security
from app.core.config import settings
from app.models.user import User
from app.schemas.auth import TokenPayload

# This scheme will extract the token from the Authorization header
# and check that its value is "Bearer <token>"
reusable_oauth2 = OAuth2PasswordBearer(
    tokenUrl=f"{settings.API_V1_STR}/auth/login"
)

def get_db() -> Generator:
    """
    Dependency to get a DB session for each request.
    """
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

def get_current_user(
    db: Session = Depends(get_db), token: str = Depends(reusable_oauth2)
) -> User:
    """
    Dependency to get the current user from a JWT token.
    """
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    payload = security.decode_token(token)
    if payload is None or payload.sub is None:
        raise credentials_exception

    user = db.query(User).filter(User.id == payload.sub).first()
    if user is None:
        raise credentials_exception

    return user

def get_current_active_user(
    current_user: User = Depends(get_current_user),
) -> User:
    """
    Dependency to get the current active user.
    Useful for endpoints that require an active user.
    """
    if not current_user.is_active:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user
