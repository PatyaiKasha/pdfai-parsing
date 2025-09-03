from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
import uuid
from typing import Any

from app.api import deps
from app.services import job_service
from app.schemas.parse import ParseJob
from app.models.user import User as UserModel

router = APIRouter()

@router.get("/{job_id}", response_model=ParseJob)
def get_job_status(
    *,
    db: Session = Depends(deps.get_db),
    job_id: uuid.UUID,
    current_user: UserModel = Depends(deps.get_current_active_user),
) -> Any:
    """
    Get the status and details of a specific parsing job.

    This endpoint allows a user to retrieve the complete details of a job they own,
    including its current status, metadata, and any results if processing is complete.
    """
    job = job_service.get_job(db=db, job_id=job_id, user=current_user)
    if not job:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Job not found or you do not have permission to view it.",
        )
    return job
