import pymongo.errors
from fastapi import APIRouter, HTTPException, status

import app.schemas.user_schema
from app.schemas.user_schema import UserAuth
from app.services.user_service import UserService

user_router = APIRouter()


@user_router.post('create', summary="Create new user", response_model=app.schemas.user_schema.UserOut)
async def create_user(data: UserAuth):
    try:
        return await UserService.create_user(data)
    except pymongo.errors.DuplicateKeyError:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="User with this email or username already exists")

    # TODO: add endpoint to update user
    # TODO: add endpoint to update user roles for admins only
    # TODO: add endpoint to update user password
