import uuid
from datetime import datetime
from sqlalchemy import Column, String, DateTime, Boolean, Integer
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from app.core.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    email = Column(String, unique=True, index=True, nullable=False)
    password_hash = Column(String, nullable=False)

    plan = Column(String, default="free", nullable=False)  # e.g., free, pro, enterprise
    usage_count = Column(Integer, default=0, nullable=False)
    usage_limit = Column(Integer, default=10, nullable=False) # Default limit for the 'free' plan

    is_active = Column(Boolean, default=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    jobs = relationship("ParseJob", back_populates="owner", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<User(email='{self.email}', plan='{self.plan}')>"
