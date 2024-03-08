from datetime import datetime, time
from typing import List, Union
from uuid import UUID

from fastapi import HTTPException

from app.models.task_model import Task
from app.models.user_model import User
from app.schemas.task_schema import TaskCreate, TaskUpdate
from .user_service import UserService
from ..utils.utils import validate_uuid, validate_date


class TaskService:
    """
    Retrieves a list of tasks created by a specific user.

    Parameters:
        - creator_id: The UUID of the user who created the tasks.

    Returns:
        - List[Task]: A list of Task objects created by the specified user.

    """
    @staticmethod
    async def list_tasks_by_creator(creator_id: UUID) -> List[Task]:
        """
            Retrieves a list of tasks created by a specific user.

            Parameters:
                - creator_id: The UUID of the user who created the tasks.

            Returns:
                - List[Task]: A list of Task objects created by the specified user.

        """
        validate_uuid(creator_id)
        user = await UserService.get_user_by_id(creator_id)
        tasks = await Task.find(Task.task_creator.id == user.id).to_list()
        return tasks

    @staticmethod
    async def list_tasks_by_assignee_id(assignee_id: UUID) -> List[Task]:
        """
        Retrieve a list of tasks based on the assignee ID.

        :param assignee_id: The ID of the assignee.
        :type assignee_id: UUID
        :return: A list of tasks assigned to the specified assignee.
        :rtype: List[Task]
        """
        validate_uuid(assignee_id)
        user = await UserService.get_user_by_id(assignee_id)
        tasks = await Task.find(Task.task_assignee.id == user.id).to_list()
        return tasks

    @staticmethod
    async def create_task(user: User, data: TaskCreate) -> Task:
        """
        Creates a new task with the provided data and associates it with the specified user.

        Parameters:
        - user (User): The user associated with the task.
        - data (TaskCreate): The data used to create the task.

        Returns:
        - Task: The newly created task.
        """
        task = Task(**data.dict(exclude_unset=True), task_creator=user)
        return await task.insert()

    @classmethod
    async def get_task_by_id(cls, task_id: UUID):
        """
        Retrieve a task by its ID.

        Parameters:
        - task_id (UUID): The unique identifier of the task.

        Returns:
        - Task: The task with the specified ID.
        """
        validate_uuid(task_id)
        task = await Task.find_one(Task.task_id == task_id)
        return task

    @classmethod
    async def update_task(cls, task_id: UUID, data: TaskUpdate) -> Task:
        """
        Updates a task with the given task_id and data.

        Parameters:
            task_id (UUID): The unique identifier of the task to update.
            data (TaskUpdate): The data to update the task with.

        Returns:
            Task: The updated task.

        Raises:
            HTTPException: If the task with the given task_id is not found.
        """
        validate_uuid(task_id)
        task = await cls.get_task_by_id(task_id=task_id)
        if not task:
            raise HTTPException(status_code=404, detail="Task not found")
        await task.update({"$set": data.dict(exclude_unset=True)})
        await task.save()
        return task

    @classmethod
    async def delete_task(cls, task_id: UUID):
        """

            Delete a task by its ID.

            Parameters:
                task_id (UUID): The ID of the task to be deleted.

            Returns:
                None: It does not return any value.

        """
        validate_uuid(task_id)
        task = await cls.get_task_by_id(task_id=task_id)
        if task:
            await task.delete()
        return None

    @staticmethod
    async def list_all_overdue_tasks() -> List[Task]:
        """List all overdue tasks.

        Returns:
            A list of Task objects that are overdue.

        """
        tasks = await Task.find(Task.due_date < datetime.utcnow()).to_list()
        return tasks

    @staticmethod
    async def list_overdue_tasks_by_assignee(assignee_id: UUID) -> List[Task]:
        """
            Retrieves a list of overdue tasks assigned to a specific assignee.

            Parameters:
                assignee_id (UUID): The ID of the assignee.

            Returns:
                List[Task]: A list of overdue Task objects.

        """
        validate_uuid(assignee_id)
        user = await UserService.get_user_by_id(assignee_id)
        tasks = await Task.find(
            Task.task_assignee.id == user.id,
            Task.due_date < datetime.utcnow()
        ).to_list()
        return tasks

    @staticmethod
    async def get_tasks_by_due_date(date: Union[str, datetime]) -> List[Task]:
        """
        Retrieve a list of tasks by their due date.

        :param date: The due date of the tasks to retrieve.
        :return: A list of tasks that are due on the specified date.
        """
        # Validate the date
        validated_date = validate_date(date)

        # Query the database to find tasks that are due on the specified date
        tasks = Task.find(Task.due_date == validated_date).to_list()

        # Construct a datetime range for the entire day
        start_of_day = datetime.combine(validated_date, time.min)
        end_of_day = datetime.combine(validated_date, time.max)

        # Query the database to find tasks that are due on the specified date, regardless of time
        tasks = Task.find(Task.due_date >= start_of_day, Task.due_date <= end_of_day).to_list()

        return tasks

    @staticmethod
    async def get_tasks_by_due_date_and_assignee(date: Union[str, datetime], assignee_id: UUID) -> List[Task]:
        """
        Returns a list of tasks filtered by due date and assignee.

        Parameters:
        - date (Union[str, datetime]): The due date to search for tasks.
          It can be either a string in the format 'YYYY-MM-DD' or a datetime object.
        - assignee_id (UUID): The ID of the assignee to filter tasks by.

        Returns:
        - List[Task]: A list of Task objects that match the given due date and assignee.

        """
        validated_date = validate_date(date)
        validate_uuid(assignee_id)

        user = await UserService.get_user_by_id(assignee_id)

        # Construct a datetime range for the entire day
        start_of_day = datetime.combine(validated_date, time.min)
        end_of_day = datetime.combine(validated_date, time.max)

        tasks = await Task.find((Task.due_date >= start_of_day) & (Task.due_date <= end_of_day) & (
                Task.task_assignee.id == user.id)).to_list()

        return tasks
