from typing import Any

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm

from app.core.security import create_access_token, create_refresh_token
from app.services.user_service import UserService

auth_router = APIRouter()


@auth_router.post("/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends()) -> Any:
    user = await UserService.authenticate(email=form_data.username, password=form_data.password)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect email or password"
        )
    # create jwt token and refresh token
    return {
        "access_token": create_access_token(str(user.user_id)),
        "refresh_token": create_refresh_token(str(user.user_id))
    }
