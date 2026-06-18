# Autoblunder SaaS

Professional content automation engine.

## Quick Start

```bash
cp .env.example .env
docker-compose up --build -d
```

- API: http://localhost:8000/api/docs
- Web: http://localhost:3000
- Worker: auto-starts with Celery

## Project Structure

- `apps/api` — FastAPI, SQLAlchemy, Celery workers
- `apps/web` — Next.js 14 dashboard
- `docker-compose.yml` — Local orchestration

## Warning

Do not implement scraped/unofficial uploaders. Use official platform APIs
or provide manual download links to remain compliant with Terms of Service.
