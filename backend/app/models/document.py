import uuid
from sqlalchemy import Column, String, Integer, JSON, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from app.core.database import Base

class Document(Base):
    __tablename__ = "documents"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    job_id = Column(UUID(as_uuid=True), ForeignKey("parse_jobs.id"), nullable=False, index=True)

    original_name = Column(String, nullable=False)
    file_size = Column(Integer, nullable=False)
    page_count = Column(Integer, nullable=False)

    document_type = Column(String, nullable=True)  # e.g., invoice, contract, report
    extracted_data = Column(JSON, nullable=True)

    job = relationship("ParseJob", back_populates="documents")

    def __repr__(self):
        return f"<Document(id={self.id}, original_name='{self.original_name}')>"
