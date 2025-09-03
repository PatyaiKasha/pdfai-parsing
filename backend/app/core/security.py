from datetime import datetime, timedelta, timezone
from typing import Any, Union

from jose import jwt, JWTError
from passlib.context import CryptContext

from app.core.config import settings
from app.schemas.auth import TokenPayload

# Password Hashing Context
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

ALGORITHM = settings.JWT_ALGORITHM

def create_access_token(
    subject: Union[str, Any], expires_delta: timedelta | None = None
) -> str:
    """
    Generates a new JWT access token.
    """
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(
            minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
        )
    to_encode = {"exp": expire, "sub": str(subject)}
    encoded_jwt = jwt.encode(to_encode, settings.JWT_SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Verifies a plain password against its hashed version.
    """
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password: str) -> str:
    """
    Hashes a plain password.
    """
    return pwd_context.hash(password)

def decode_token(token: str) -> TokenPayload | None:
    """
    Decodes a JWT token and returns its payload.
    """
    try:
        payload = jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=[ALGORITHM])
        return TokenPayload(**payload)
    except JWTError:
        return None
