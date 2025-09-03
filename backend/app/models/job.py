import uuid
from datetime import datetime
from sqlalchemy import Column, String, DateTime, ForeignKey, JSON
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from app.core.database import Base

class ParseJob(Base):
    __tablename__ = "parse_jobs"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False, index=True)

    filename = Column(String, nullable=False)
    file_url = Column(String, nullable=False)

    status = Column(String, default="pending", nullable=False, index=True) # pending, processing, completed, failed
    result_data = Column(JSON, nullable=True)

    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    completed_at = Column(DateTime, nullable=True)
    error_message = Column(String, nullable=True)

    owner = relationship("User", back_populates="jobs")
    documents = relationship("Document", back_populates="job", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<ParseJob(id={self.id}, filename='{self.filename}', status='{self.status}')>"
