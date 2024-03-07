from typing import List
from uuid import UUID

from fastapi import HTTPException

from app.models.task_model import Task
from app.models.user_model import User
from app.schemas.task_schema import TaskCreate, TaskUpdate


class TaskService:
    @staticmethod
    async def list_tasks(user: User) -> List[Task]:
        tasks = await Task.find(Task.task_creator.id == user.id).to_list()
        return tasks

    @staticmethod
    async def create_task(user: User, data: TaskCreate) -> Task:
        task = Task(**data.dict(exclude_unset=True), task_creator=user)
        return await task.insert()

    @classmethod
    async def get_task_by_id(cls, task_id: UUID):
        task = await Task.find_one(Task.task_id == task_id)
        return task

    @classmethod
    async def update_task(cls, task_id: UUID, data: TaskUpdate) -> Task:
        try:
            task_id
        except ValueError:
            raise ValueError("Invalid task id provided.")

        task = await TaskService.get_task_by_id(task_id=task_id)

        if not task:
            raise HTTPException(status_code=404, detail="Task not found")

        await task.update({"$set": data.dict(exclude_unset=True)})
        await task.save()

        return task

    @staticmethod
    async def delete_task(task_id: UUID):
        task = await TaskService.get_task_by_id(task_id=task_id)
        if task:
            await task.delete()
        return None
