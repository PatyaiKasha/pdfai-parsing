import uuid
from datetime import datetime
from pydantic import BaseModel
from typing import Any, List

# --- Document Schemas ---

class DocumentBase(BaseModel):
    original_name: str
    file_size: int
    page_count: int
    document_type: str | None = None

class DocumentCreate(DocumentBase):
    job_id: uuid.UUID
    extracted_data: dict | None = None

class Document(DocumentBase):
    id: uuid.UUID
    job_id: uuid.UUID

    class Config:
        from_attributes = True

# --- ParseJob Schemas ---

class ParseJobBase(BaseModel):
    filename: str
    file_url: str

class ParseJobCreate(ParseJobBase):
    pass # user_id will be taken from the current logged-in user

class ParseJobUpdate(BaseModel):
    status: str | None = None
    result_data: dict | None = None
    error_message: str | None = None

class ParseJob(ParseJobBase):
    id: uuid.UUID
    user_id: uuid.UUID
    status: str
    created_at: datetime
    completed_at: datetime | None = None
    error_message: str | None = None
    result_data: Any | None = None

    class Config:
        from_attributes = True
