from typing import Optional
from uuid import UUID

from fastapi import HTTPException

from app.core.security import get_password, verify_password
from app.models.user_model import User
from app.schemas.user_schema import UserAuth, UserUpdate
from ..utils.utils import validate_uuid


class UserService:
    @staticmethod
    async def create_user(user: UserAuth):
        """
        Create User

        :param user: The user object containing the user information
        :type user: UserAuth
        :return: The created user object
        :rtype: User
        """
        user_in = User(
            username=user.username,
            email=user.email,
            hashed_password=get_password(user.password),
            roles=user.roles
        )
        await user_in.save()
        return user_in

    @staticmethod
    async def get_user_by_email(email: str) -> Optional[User]:
        """
        Retrieve a user by their email address.

        :param email: The email address of the user.
        :return: The user object if found, otherwise None.
        """
        user = await User.find_one(User.email == email)
        return user

    @staticmethod
    async def get_user_by_id(user_id: UUID) -> Optional[User]:
        """
        Return a user object based on the provided user ID.

        :param user_id: Unique identifier for the user.
        :type user_id: UUID
        :return: User object if user is found, otherwise None.
        :rtype: Optional[User]
        """
        user = await User.find_one(User.user_id == user_id)
        return user

    @staticmethod
    async def authenticate(email: str, password: str) -> Optional[User]:
        """
        Authenticates a user.

        :param email: The email of the user.
        :param password: The password of the user.
        :return: The authenticated user object if successful, otherwise None.
        """
        user = await UserService.get_user_by_email(email=email)
        if not user:
            return None
        if not verify_password(password=password, hashed_password=user.hashed_password):
            return None

        return user

    @classmethod
    async def update_user_by_id(cls, user_id: UUID, user_update: UserUpdate) -> User:
        """
        Update user by ID.

        :param user_id: The ID of the user to update.
        :param user_update: The updated user information.
        :return: The updated user object.
        """
        validate_uuid(user_id)
        user = await cls.get_user_by_id(user_id=user_id)
        if not user:
            raise HTTPException(status_code=404, detail="Task not found")

        await user.update({"$set": user_update.dict(exclude_unset=True)})
        await user.save()

        return user

    # TODO: add method to update user password
    # TODO: add method to update user roles, only for admins
