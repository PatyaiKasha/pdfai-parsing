from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List, Any

from app.api import deps
from app.services import users_service
from app.schemas.user import User, UserUpdate
from app.schemas.parse import ParseJob
from app.models.user import User as UserModel

router = APIRouter()

@router.get("/profile", response_model=User)
def get_user_profile(
    current_user: UserModel = Depends(deps.get_current_active_user),
) -> Any:
    """
    Retrieve the profile for the currently authenticated user.
    """
    return current_user

@router.put("/profile", response_model=User)
def update_user_profile(
    *,
    db: Session = Depends(deps.get_db),
    user_in: UserUpdate,
    current_user: UserModel = Depends(deps.get_current_active_user),
) -> Any:
    """
    Update the profile for the currently authenticated user.
    """
    user = users_service.update_user(db=db, db_user=current_user, user_in=user_in)
    return user

@router.get("/usage", response_model=dict)
def get_user_usage(
    current_user: UserModel = Depends(deps.get_current_active_user),
) -> Any:
    """
    Get the current user's API usage and plan limits.
    """
    return {
        "usage_count": current_user.usage_count,
        "usage_limit": current_user.usage_limit,
        "plan": current_user.plan,
    }

@router.get("/history", response_model=List[ParseJob])
def get_user_history(
    db: Session = Depends(deps.get_db),
    current_user: UserModel = Depends(deps.get_current_active_user),
) -> Any:
    """
    Retrieve the job history for the currently authenticated user.
    """
    jobs = users_service.get_user_jobs(db=db, user_id=current_user.id)
    return jobs
