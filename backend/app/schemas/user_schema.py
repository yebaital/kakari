from typing import Optional, List
from uuid import UUID

from pydantic import BaseModel, EmailStr, Field


class UserAuth(BaseModel):
    email: EmailStr = Field(..., description="User email")
    username: str = Field(..., min_length=5, max_length=50,
                          description="User username")
    password: str = Field(..., min_length=6, max_length=24,
                          description="User password")
    roles: List[str] = Field(["user"], description="User roles")


class UserOut(BaseModel):
    user_id: UUID
    username: str
    email: EmailStr
    first_name: Optional[str]
    last_name: Optional[str]
    disabled: Optional[bool] = False
    roles: List[str]
