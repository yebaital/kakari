from beanie import init_beanie
from fastapi import FastAPI
from fastapi.concurrency import asynccontextmanager
from fastapi.middleware.cors import CORSMiddleware
from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.server_api import ServerApi

from .api.v1.router import router
from .core.config import settings
from .models.task_model import Task
from .models.user_model import User


async def init():
    client = AsyncIOMotorClient(f"mongodb+srv://{settings.MONGO_USERNAME}:{settings.MONGO_PASSWORD}@kakari.4fzslk7.mongodb.net/?retryWrites=true&w=majority&appName=Kakari", server_api=ServerApi('1'))
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

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.BACKEND_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router, prefix=settings.API_V1_STR)
