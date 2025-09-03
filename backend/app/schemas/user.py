import uuid
from datetime import datetime
from pydantic import BaseModel, EmailStr

# Shared properties
class UserBase(BaseModel):
    email: EmailStr

# Properties to receive via API on creation
class UserCreate(UserBase):
    password: str

# Properties to receive via API on update
class UserUpdate(BaseModel):
    email: EmailStr | None = None
    # Add other fields that can be updated, e.g., plan
    plan: str | None = None

# Base model for properties stored in DB
class UserInDBBase(UserBase):
    id: uuid.UUID
    is_active: bool
    plan: str
    usage_count: int
    usage_limit: int
    created_at: datetime

    class Config:
        from_attributes = True

# Properties to return to client
class User(UserInDBBase):
    pass

# Properties stored in DB
class UserInDB(UserInDBBase):
    password_hash: str
