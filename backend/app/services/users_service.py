from sqlalchemy.orm import Session
from typing import List, Optional

from app.models.user import User
from app.models.job import ParseJob
from app.schemas.user import UserUpdate

def get_user(db: Session, user_id: str) -> Optional[User]:
    """
    Get a single user by their ID.
    """
    return db.query(User).filter(User.id == user_id).first()

def update_user(db: Session, *, db_user: User, user_in: UserUpdate) -> User:
    """
    Update a user's profile information.
    """
    # Get the dictionary of fields to update, excluding unset values
    user_data = user_in.model_dump(exclude_unset=True)

    # Update the user object with the new data
    for field, value in user_data.items():
        setattr(db_user, field, value)

    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user_jobs(db: Session, *, user_id: str) -> List[ParseJob]:
    """
    Get a list of a user's parsing jobs, ordered by creation date.
    """
    return db.query(ParseJob).filter(ParseJob.user_id == user_id).order_by(ParseJob.created_at.desc()).all()
