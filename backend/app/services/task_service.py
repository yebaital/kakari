from typing import List
from uuid import UUID

from fastapi import HTTPException

from app.models.task_model import Task
from app.models.user_model import User
from app.schemas.task_schema import TaskCreate, TaskUpdate


class TaskService:
    @staticmethod
    async def list_tasks(user: User) -> List[Task]:
        """
        List tasks created by a user.

        :param user: The user for whom to list tasks.
        :return: A list of tasks created by the user.
        :rtype: list
        """
        tasks = await Task.find(Task.task_creator.id == user.id).to_list()
        return tasks

    @staticmethod
    async def create_task(user: User, data: TaskCreate) -> Task:
        """
        Create a new task.

        :param user: The user who is creating the task.
        :param data: The data for creating the task (TaskCreate object).
        :return: The created task (Task object).
        """
        task = Task(**data.dict(exclude_unset=True), task_creator=user)
        return await task.insert()

    @classmethod
    async def get_task_by_id(cls, task_id: UUID):
        """
        Retrieves a task by its ID.

        :param task_id: The ID of the task to retrieve.
        :return: The task object if found, None otherwise.
        """
        task = await Task.find_one(Task.task_id == task_id)
        return task

    @classmethod
    async def update_task(cls, task_id: UUID, data: TaskUpdate) -> Task:
        """
        Updates a task with the given task_id using the provided data.

        :param task_id: The UUID of the task to be updated.
        :param data: The TaskUpdate object containing the updated data for the task.
        :return: The updated Task object.
        :raises ValueError: If an invalid task_id is provided.
        :raises HTTPException: If the task is not found.
        """
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
        """
        Delete a task by task ID.

        :param task_id: The ID of the task to be deleted.
        :return: None.
        """
        task = await TaskService.get_task_by_id(task_id=task_id)
        if task:
            await task.delete()
        return None
