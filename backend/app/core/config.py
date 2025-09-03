from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    """
    Application settings loaded from the environment.
    """
    # Core settings
    PROJECT_NAME: str = "AI PDF Parser API"
    API_V1_STR: str = "/api/v1"

    # Environment file
    model_config = SettingsConfigDict(env_file=".env", case_sensitive=True, extra="ignore")

    # Database
    DATABASE_URL: str

    # Redis
    REDIS_URL: str

    # S3 Storage
    S3_BUCKET: str
    S3_ACCESS_KEY_ID: str | None = None
    S3_SECRET_ACCESS_KEY: str | None = None
    S3_ENDPOINT_URL: str | None = None  # For MinIO

    # AI Services
    OPENAI_API_KEY: str

    # JWT
    JWT_SECRET_KEY: str
    JWT_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24  # 1 day

settings = Settings()
