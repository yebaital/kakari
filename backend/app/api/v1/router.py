from fastapi import APIRouter

from app.api.auth.jwt import auth_router
from app.api.v1.handlers import user, task

router = APIRouter()
router.include_router(user.user_router, prefix="/user", tags=["user"])
router.include_router(auth_router, prefix="/auth", tags=["auth"])
router.include_router(task.task_router, prefix="/task", tags=["task"])

# TODO: add project router
