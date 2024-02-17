from typing import Optional
from uuid import UUID

from pydantic import BaseModel, EmailStr, Field


class UserAuth(BaseModel):
    email: EmailStr = Field(..., description="User email")
    username: str = Field(..., min_length=5, max_length=50,
                          description="User username")
    password: str = Field(..., min_length=6, max_length=24,
                          description="User password")


class UserOut(BaseModel):
    user_id: UUID
    username: str
    email: EmailStr
    first_name: Optional[str]
    last_name: Optional[str]
    disabled: Optional[bool] = False
