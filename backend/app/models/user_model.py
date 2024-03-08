import datetime
from beanie import Document, Indexed
from pydantic import Field, EmailStr
from uuid import UUID, uuid4
from typing import Optional, List


class User(Document):
    user_id: UUID = Field(default_factory=uuid4)
    email: Indexed(EmailStr, unique=True)
    hashed_password: str
    full_name: Optional[str] = None
    disabled: Optional[bool] = None
    activated: Optional[bool] = None
    roles: List[str] = Field(default_factory=list)

    def __repr__(self) -> str:
        return f"<User {self.email}>"

    def __str__(self) -> str:
        return self.email

    def __hash__(self) -> int:
        return hash(self.email)

    def __eq__(self, other: object) -> bool:
        if isinstance(other, User):
            return self.email == other.email
        return False

    """
        If called on instance, gives us the date/time the user was created
    """
    @property
    def create(self) -> datetime:
        return self.id.generation_time

    """
        Gets user by email
    """
    @classmethod
    async def by_email(self, email: str) -> "User":
        return await self.find_one(self.email == email)

    class Settings:
        name = "users"
