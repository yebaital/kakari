from typing import List
from uuid import UUID, uuid4

from beanie import Document, Indexed, Link
from pydantic import Field

from app.models.task_model import Task
from app.models.user_model import User


class Project(Document):
    project_id: UUID = Field(default_factory=uuid4, unique=True)
    project_name: Indexed(str)
    description: str = None
    project_owner: Link[User]
    project_members: List[Link[User]]
    tasks: List[Link[Task]]
