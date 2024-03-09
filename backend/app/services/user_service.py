from typing import Optional, List
from uuid import UUID

from fastapi import HTTPException, Depends

from app.core.security import get_password, verify_password
from app.models.user_model import User
from app.schemas.user_schema import UserAuth, UserUpdate
from ..api.deps.user_deps import get_current_user
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
    async def update_user_by_id(cls, user_id: UUID, user_update: UserUpdate,
                                current_user=Depends(get_current_user)) -> User:
        """
        Updates a user by their ID.

        Parameters:
        - user_id: UUID - The ID of the user to update.
        - user_update: UserUpdate - The updated user data to apply.
        - current_user (optional): Depends - The current user making the request. Defaults to the result of the `get_current_user` function.

        Returns:
        - User - The updated user object.

        Raises:
        - HTTPException - If the user with the given ID is not found or if the current user is unauthorized.
        """
        validate_uuid(user_id)
        user = await cls.get_user_by_id(user_id=user_id)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")

        if user is current_user or "admin" in current_user.roles:
            await user.update({"$set": user_update.dict(exclude_unset=True)})
            await user.save()
        else:
            raise HTTPException(status_code=401, detail="Unauthorized")

        return user

    # TODO: add method to update user password
    @classmethod
    async def update_user_roles(cls, user_id: UUID, current_user: Depends(get_current_user),
                                user_roles: List[str]) -> User:
        """
            Update User Roles method.

            Parameters:
            - user_id (UUID): The UUID of the user to update.
            - current_user (Depends(get_current_user)): The current authenticated user.
            - user_roles (List[str]): The new roles to assign to the user.

            Returns:
            - User: The updated user instance.

            Raises:
            - HTTPException - 404: If the user is not found.
            - HTTPException - 401: If the current user does not have admin privileges.
        """
        user = await cls.get_user_by_id(user_id=user_id)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")

        if "admin" in current_user.roles:
            user.roles = user_roles
            await user.save()

        else:
            raise HTTPException(status_code=401, detail="Unauthorized")

        return user
