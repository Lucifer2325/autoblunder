from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql+psycopg2://autoblunder:autoblunder@localhost:5432/autoblunder"
    REDIS_URL: str = "redis://localhost:6379/0"
    CORS_ORIGINS: list[str] = ["http://localhost:3000"]
    SECRET_KEY: str = "dev-secret-change-me"

    class Config:
        env_file = ".env"


settings = Settings()
