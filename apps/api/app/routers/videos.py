from fastapi import APIRouter
from pydantic import BaseModel


router = APIRouter()


class GenerateRequest(BaseModel):
    script: str
    style: str = "minecraft_parkour"


class GenerateResponse(BaseModel):
    job_id: str
    status: str
    message: str


@router.post("/generate", response_model=GenerateResponse)
async def generate_video(req: GenerateRequest):
    from app.core.engine import create_render_job
    from app.tasks.worker import render_video_task

    job_id = create_render_job(req.script, req.style)

    # Queue background render
    render_video_task.delay(
        {"job_id": job_id, "script": req.script, "style": req.style}
    )

    return GenerateResponse(
        job_id=job_id,
        status="queued",
        message="Video render job accepted."
    )
