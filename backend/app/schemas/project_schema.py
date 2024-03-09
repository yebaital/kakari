from typing import Optional, List

from beanie import Link
from pydantic import BaseModel, Field

from app.models.task_model import Task
from app.models.user_model import User


class ProjectCreate(BaseModel):
    project_name: str = Field(..., title="Project Title", max_length=55, min_length=3, examples=["Project Title"])
    description: Optional[str] = None
    project_owner: Link[User]
    project_members: Optional[List[Link[User]]] = None
    tasks: Optional[List[Link[Task]]] = None


class ProjectUpdate(BaseModel):
    project_name: str = Field(..., title="Project Title", max_length=55, min_length=3, examples=["Project Title"])
    description: Optional[str] = None
    project_members: Optional[List[Link[User]]] = None
    tasks: Optional[List[Link[Task]]] = None
