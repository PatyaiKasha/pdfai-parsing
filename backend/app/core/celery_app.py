from celery import Celery
from app.core.config import settings

# Initialize the Celery application
celery_app = Celery(
    "worker",
    broker=settings.REDIS_URL,
    backend=settings.REDIS_URL,  # Using Redis as the result backend as well
    include=["app.workers.pdf_worker"]  # List of modules to import when the worker starts
)

# Optional configuration
celery_app.conf.update(
    task_track_started=True,
    broker_connection_retry_on_startup=True,
)
