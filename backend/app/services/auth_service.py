from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserCreate
from app.core.security import get_password_hash, verify_password

def get_user_by_email(db: Session, *, email: str) -> User | None:
    """
    Fetches a user by their email address.
    """
    return db.query(User).filter(User.email == email).first()

def create_user(db: Session, *, user_in: UserCreate) -> User:
    """
    Creates a new user in the database.
    """
    hashed_password = get_password_hash(user_in.password)
    db_user = User(
        email=user_in.email,
        password_hash=hashed_password,
    )
    # Default values for plan, usage_count, etc., are set in the User model
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def authenticate_user(db: Session, *, email: str, password: str) -> User | None:
    """
    Authenticates a user. Returns the user object if successful, else None.
    """
    user = get_user_by_email(db, email=email)
    if not user:
        return None
    if not verify_password(password, user.password_hash):
        return None
    return user
