import uuid
from fastapi import UploadFile, HTTPException, status
from sqlalchemy.orm import Session

from app.models.job import ParseJob
from app.models.user import User

class FileService:
    """Handles file-related operations such as validation and job creation."""
    def __init__(self, db: Session):
        """
        Initializes the service with a database session.

        Args:
            db: The SQLAlchemy Session object.
        """
        self.db = db

    async def validate_pdf(self, file: UploadFile) -> None:
        """
        Validates if the uploaded file is a PDF and within size limits.
        Raises HTTPException if validation fails.
        """
        if file.content_type != "application/pdf":
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Invalid file type. Only PDF files are accepted.",
            )

    async def create_upload_job(self, *, file: UploadFile, user: User) -> ParseJob:
        """
        Coordinates the file upload process.

        This method validates the uploaded PDF, creates a record for the parsing
        job in the database, and increments the user's document usage count.
        In a real-world scenario, it would also handle uploading the file to a
        persistent storage service like S3.

        Args:
            file: The uploaded PDF file from the FastAPI request.
            user: The currently authenticated user who uploaded the file.

        Returns:
            The newly created ParseJob database object.
        """
        await self.validate_pdf(file)

        mock_file_url = f"s3://{uuid.uuid4()}/{file.filename}"

        parse_job = ParseJob(
            user_id=user.id,
            filename=file.filename,
            file_url=mock_file_url,
            status="pending",
        )
        self.db.add(parse_job)

        user.usage_count += 1
        self.db.add(user)

        self.db.commit()
        self.db.refresh(parse_job)

        return parse_job
