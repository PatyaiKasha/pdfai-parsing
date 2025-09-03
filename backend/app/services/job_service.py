from sqlalchemy.orm import Session
import uuid
from typing import Optional

from app.models.job import ParseJob
from app.models.user import User

def get_job(db: Session, *, job_id: uuid.UUID, user: User) -> Optional[ParseJob]:
    """
    Get a job by its ID.

    This function ensures that the job belongs to the requesting user,
    preventing users from accessing jobs that are not their own.

    Args:
        db: The database session.
        job_id: The ID of the job to retrieve.
        user: The currently authenticated user.

    Returns:
        The ParseJob object if found and owned by the user, otherwise None.
    """
    return db.query(ParseJob).filter(ParseJob.id == job_id, ParseJob.user_id == user.id).first()
