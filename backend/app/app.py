from beanie import init_beanie
from fastapi import FastAPI
from fastapi.concurrency import asynccontextmanager
from motor.motor_asyncio import AsyncIOMotorClient

from .api.v1.router import router
from .core.config import settings
from .models.task_model import Task
from .models.user_model import User


async def init():
    client = AsyncIOMotorClient(settings.MONGO_CONNECTION_STRING)
    db = client.kakari
    await init_beanie(database=db, document_models=[User, Task])


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
