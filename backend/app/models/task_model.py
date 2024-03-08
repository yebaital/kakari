from datetime import datetime
from enum import Enum
from typing import Any, List
from uuid import UUID, uuid4

from beanie import Document, Indexed, Link, Replace, before_event, Insert
from pydantic import Field

from app.models.task_comment_model import TaskComment
from app.models.user_model import User


class StatusEnum(str, Enum):
    NOT_STARTED = "Not Started"
    UNDER_PROCESS = "Under Process"
    COMPLETED = "Completed"


class Task(Document):
    task_id: UUID = Field(default_factory=uuid4, unique=True)
    complete: bool = False
    status: StatusEnum = StatusEnum.NOT_STARTED
    title: Indexed(str)
    description: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
    due_date: datetime = Field(default_factory=datetime.utcnow)
    task_creator: Link[User]
    task_assignee: Link[User] = None
    comments: List[Link[TaskComment]] = []

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, Task):
            return self.task_id == other.task_id
        return False

    def __repr__(self) -> str:
        return f"<Task: {self.title}>"

    def __str__(self) -> str:
        return self.title

    def __hash__(self):
        return hash(self.title)

    """
    At the time of updating, update updated_at
    """

    @before_event([Replace, Insert])
    def update_updated_at(self):
        self.updated_at = datetime.utcnow()

    class Settings:
        name = "tasks"
