from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings
from app.routers import health, videos


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup: run alembic or db init here if needed
    yield
    # Shutdown: close connections


app = FastAPI(
    title="Autoblunder API",
    version="1.0.0",
    docs_url="/api/docs",
    redoc_url="/api/redoc",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health.router, tags=["system"])
app.include_router(videos.router, prefix="/api/v1/videos", tags=["videos"])
