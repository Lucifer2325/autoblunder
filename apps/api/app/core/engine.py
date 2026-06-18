"""
Video generation engine.
DO NOT implement scraping uploaders here. Use official APIs only
or expose a manual download endpoint.
"""

import uuid
from pathlib import Path


def create_render_job(script: str, style: str) -> str:
    """
    Pushes a render into the queue.
    Returns a job_id for polling.
    """
    job_id = str(uuid.uuid4())
    # TODO: Save job to DB, queue Celery task
    return job_id


def render_video(job_id: str, script: str, style: str) -> Path:
    """
    Runs MoviePy/FFmpeg to build the final MP4.
    This runs inside the Celery worker.
    """
    output_path = Path(f"/tmp/{job_id}.mp4")
    # TODO: Implement actual FFmpeg/MoviePy render pipeline
    # 1. Fetch/style gameplay footage based on `style`
    # 2. Run TTS on `script`
    # 3. Burn subtitles (fast cuts, high contrast)
    # 4. Mix audio and write to output_path
    return output_path
