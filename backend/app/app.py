from fastapi import FastAPI
from fastapi.concurrency import asynccontextmanager
from app.core.config import settings
from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient
from app.models.user_model import User
from app.api.v1.router import router


async def init():
    client = AsyncIOMotorClient(settings.MONGO_CONNECTION_STRING)
    db = client.kakari
    await init_beanie(database=db, document_models=[User])


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init()
    yield

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
    lifespan=lifespan
)

app.include_router(router, prefix=settings.API_V1_STR)
