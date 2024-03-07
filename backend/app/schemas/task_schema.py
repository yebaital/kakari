from datetime import datetime
from typing import Optional
from uuid import UUID

from beanie import Link
from pydantic import BaseModel, Field

from app.models.task_model import StatusEnum
from app.models.user_model import User


class TaskCreate(BaseModel):
    title: str = Field(..., title='Title', max_length=55, min_length=3)
    description: str = Field(..., title='Title', max_length=755, min_length=3)
    complete: Optional[bool] = False
    due_date: Optional[datetime] = None
    task_assignee: Optional[Link[User]] = None


class TaskUpdate(BaseModel):
    title: Optional[str] = Field(None, title='Title', max_length=55, min_length=3)
    description: Optional[str] = Field(None, title='Description', max_length=755, min_length=3)
    complete: Optional[bool] = False
    status: Optional[StatusEnum] = None
    due_date: Optional[datetime] = None
    task_assignee: Optional[Link[User]] = None


class TaskOut(BaseModel):
    task_id: UUID
    complete: bool
    title: str
    description: str
    created_at: datetime
    updated_at: datetime
    task_assignee: Link[User]
