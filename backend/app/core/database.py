from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.core.config import settings

# Create the SQLAlchemy engine using the database URL from settings
engine = create_engine(
    settings.DATABASE_URL,
    # connect_args={"check_same_thread": False} # This is needed for SQLite, not for PostgreSQL
)

# Create a configured "Session" class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a Base class for declarative class definitions
Base = declarative_base()
