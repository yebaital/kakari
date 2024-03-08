from typing import Optional, List
from uuid import UUID

from pydantic import BaseModel, EmailStr, Field


class UserAuth(BaseModel):
    email: EmailStr = Field(..., description="User email")
    password: str = Field(..., min_length=6, max_length=24,
                          description="User password")
    roles: List[str] = Field(["user"], description="User roles")


class UserOut(BaseModel):
    user_id: UUID
    email: EmailStr
    full_name: Optional[str]
    disabled: Optional[bool] = False
    activated: Optional[bool] = False
    roles: List[str]


class UserUpdate(BaseModel):
    id: Optional[UUID] = Field(None, description="User ID")
    email: Optional[EmailStr] = Field(None, description="User email")
    full_name: Optional[str] = Field(None, description="Full name")
    disabled: Optional[bool] = Field(None, description="User disabled status")
    activated: Optional[bool] = Field(None, description="User activated status")
