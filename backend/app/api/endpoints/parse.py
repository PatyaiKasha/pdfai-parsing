from fastapi import APIRouter, Depends, UploadFile, File, HTTPException, status
from sqlalchemy.orm import Session
from typing import Any

from app.api import deps
from app.services.file_service import FileService
from app.schemas.parse import ParseJob
from app.models.user import User as UserModel

router = APIRouter()

@router.post("/upload", response_model=ParseJob, status_code=status.HTTP_202_ACCEPTED)
async def upload_pdf_for_parsing(
    *,
    db: Session = Depends(deps.get_db),
    current_user: UserModel = Depends(deps.get_current_active_user),
    file: UploadFile = File(...),
) -> Any:
    """
    Upload a PDF file for asynchronous parsing.

    This endpoint accepts a PDF file, validates it, checks user usage limits,
    and creates a background job for processing. It returns immediately with
    the job details.
    """
    if current_user.usage_count >= current_user.usage_limit:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Usage limit exceeded. Please upgrade your plan.",
        )

    file_service = FileService(db)
    parse_job = await file_service.create_upload_job(file=file, user=current_user)

    # Dispatch the background task to the Celery worker.
    # We convert the job_id to a string as it's a best practice for Celery arguments.
    from app.workers.pdf_worker import process_pdf_task
    process_pdf_task.delay(str(parse_job.id))

    return parse_job
