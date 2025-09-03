from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from typing import Any

from app.api import deps
from app.core import security
from app.services import auth_service
from app.schemas.user import User
from app.schemas.auth import Token
from app.schemas.user import UserCreate

router = APIRouter()

@router.post("/register", response_model=User, status_code=status.HTTP_201_CREATED)
def register_user(
    *,
    db: Session = Depends(deps.get_db),
    user_in: UserCreate,
) -> Any:
    """
    Create a new user.
    """
    user = auth_service.get_user_by_email(db, email=user_in.email)
    if user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="The user with this email already exists in the system.",
        )
    new_user = auth_service.create_user(db, user_in=user_in)
    return new_user


@router.post("/login", response_model=Token)
def login_for_access_token(
    db: Session = Depends(deps.get_db), form_data: OAuth2PasswordRequestForm = Depends()
) -> Any:
    """
    OAuth2 compatible token login, get an access token for future requests.
    """
    user = auth_service.authenticate_user(
        db, email=form_data.username, password=form_data.password
    )
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    if not user.is_active:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Inactive user")

    access_token = security.create_access_token(subject=user.id)
    return {
        "access_token": access_token,
        "token_type": "bearer",
    }


@router.get("/me", response_model=User)
def read_user_me(
    current_user: User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Get current user.
    """
    return current_user
