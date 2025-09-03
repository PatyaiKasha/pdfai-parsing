import time
import random
import uuid
from datetime import datetime

from app.core.celery_app import celery_app
from app.core.database import SessionLocal
from app.models.job import ParseJob

@celery_app.task(acks_late=True)
def process_pdf_task(job_id: str):
    """
    A Celery task to simulate AI-powered PDF processing.
    """
    db = SessionLocal()
    try:
        job_uuid = uuid.UUID(job_id)
        job = db.query(ParseJob).filter(ParseJob.id == job_uuid).first()

        if not job:
            # Job may have been deleted before the worker picked it up.
            print(f"Job with id {job_id} not found. Aborting task.")
            return

        # 1. Update status to "processing" to show work has started.
        job.status = "processing"
        db.commit()

        # 2. Simulate a long-running AI/OCR process.
        processing_time = random.randint(10, 25)
        time.sleep(processing_time)

        # 3. Simulate success or failure of the processing.
        if random.random() < 0.9:  # 90% success rate
            # On success, update status and add mock result data.
            job.status = "completed"
            job.result_data = {
                "document_type": random.choice(["invoice", "contract", "report", "receipt"]),
                "extracted_fields": {
                    "total_amount": round(random.uniform(50, 7500), 2),
                    "invoice_date": "2025-09-03",
                    "vendor_name": "Mock AI Vendor Corp."
                },
                "confidence_score": round(random.uniform(0.85, 0.99), 2),
                "pages_processed": random.randint(1, 20),
            }
        else:
            # On failure, update status and add an error message.
            job.status = "failed"
            job.error_message = "AI model failed to converge on a result or confidence was too low."

        job.completed_at = datetime.utcnow()
        db.commit()

    except Exception as e:
        # Broad exception catch to ensure any failure is logged to the job.
        db.rollback()
        # Re-fetch job in a new transaction to update it
        job = db.query(ParseJob).filter(ParseJob.id == uuid.UUID(job_id)).first()
        if job:
            job.status = "failed"
            job.error_message = f"An unexpected error occurred: {str(e)}"
            job.completed_at = datetime.utcnow()
            db.commit()
    finally:
        # Ensure the database session is always closed.
        db.close()

    return f"Job {job_id} processing finished with status: {job.status}"
