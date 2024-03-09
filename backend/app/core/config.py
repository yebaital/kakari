from pydantic import AnyHttpUrl
from pydantic_settings import BaseSettings
from decouple import config
from typing import List


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    JWT_SECRET_KEY: str = config("JWT_SECRET_KEY", cast=str)
    JWT_REFRESH_SECRET_KEY: str = config("JWT_REFRESH_SECRET_KEY", cast=str)
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRATION_MINUTES: int = 15
    # 7 days
    REFRESH_TOKEN_EXPIRATION_MINUTES: int = 60 * 24 * 7
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []
    PROJECT_NAME: str = "KAKARI"
    MONGO_CONNECTION_STRING: str = config("MONGO_CONNECTION_STRING", cast=str)
    MAILTRAP_USERNAME: str = config("MAILTRAP_USERNAME")
    MAILTRAP_PASSWORD: str = config("MAILTRAP_PASSWORD")
    BASE_URL: str = config("BASE_URL")


class Config:
    case_sensitive = True


settings = Settings()
