from celery import Celery
from app.core.config import settings

celery_app = Celery("tasks", broker=settings.REDIS_URL, backend=settings.REDIS_URL)


@celery_app.task(bind=True, max_retries=3)
def render_video_task(self, job_data: dict):
    """
    Celery task that calls the engine.
    """
    try:
        from app.core.engine import render_video
        output = render_video(
            job_data["job_id"], job_data["script"], job_data["style"]
        )
        return {"status": "success", "file": str(output)}
    except Exception as exc:
        raise self.retry(exc=exc, countdown=60)
