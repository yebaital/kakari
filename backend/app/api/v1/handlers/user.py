from typing import List
from uuid import UUID

import pymongo.errors
from fastapi import APIRouter, HTTPException, status, Depends

from app.api.deps.user_deps import get_current_user
from app.schemas.user_schema import UserAuth
from app.schemas.user_schema import UserOut, UserUpdate
from app.services.user_service import UserService
from app.utils.utils import validate_uuid

user_router = APIRouter()


# TODO: add endpoint to update user roles for admins only
# TODO: add endpoint to update user password

@user_router.post('/create', summary="Create new user", response_model=UserOut)
async def create_user(data: UserAuth):
    """
    Create new user.

    Args:
        data (UserAuth): The user authentication data.

    Returns:
        UserOut: The created user data.

    Raises:
        HTTPException: If the user with the given email or username already exists.
    """
    try:
        return await UserService.create_user(data)
    except pymongo.errors.DuplicateKeyError:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="User with this email or username already exists")


@user_router.put('/', summary="Update user", response_model=UserOut)
async def update_user(user_id: UUID, data: UserUpdate):
    """
    Update user.

    Parameters:
    - user_id (UUID): The ID of the user to update.
    - data (UserUpdate): The data with which to update the user.

    Returns:
    - UserOut: The updated user.
    """
    validate_uuid(user_id)
    return await UserService.update_user_by_id(user_id=user_id, user_update=data)


@user_router.put('/update-roles/{user_id}', summary="Update user roles", response_model=UserOut)
async def update_user_roles(user_id: UUID, roles: List[str], current_user: Depends(get_current_user)):
    """
    Update User Roles

    Update the roles of a user identified by their user ID.

    Parameters:
    - user_id (UUID): The unique identifier of the user.
    - roles (List[str]): A list of role names to be assigned to the user.
    - current_user: The currently authenticated user making the request.

    Returns:
    - UserOut: The updated user object with the modified roles.
    """
    return await UserService.update_user_roles(user_id=user_id, user_roles=roles, current_user=current_user)
