from datetime import datetime

from beanie import Document, Link
from pydantic import Field

from app.models.user_model import User


class TaskComment(Document):
    content: str
    author: Link[User]
    created_at: datetime = Field(default_factory=datetime.utcnow)

    def __repr__(self) -> str:
        return f"<Comment by {self.author}: {self.content}>"

    class Settings:
        name = "task_comments"
