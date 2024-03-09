from datetime import datetime
from typing import List
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException

from app.api.deps.user_deps import get_current_user
from app.models.task_model import Task
from app.models.user_model import User
from app.schemas.task_schema import TaskOut, TaskCreate, TaskUpdate
from app.services.task_service import TaskService

task_router = APIRouter()


@task_router.get('/created/{user_id}', summary="Get all tasks created by user", response_model=List[TaskOut])
async def list_user_created_tasks(user_id: UUID):
    """
    Get all tasks created by a user.

    Args:
        user_id (UUID): The ID of the user.

    Returns:
        List[TaskOut]: A list of tasks created by the user.
    """
    return await TaskService.list_tasks_by_creator(user_id)


@task_router.post('create', summary="Create a new task", response_model=TaskOut)
async def create_task(data: TaskCreate, current_user: User = Depends(get_current_user)):
    """
    Create a new task.

    :param data: The data required to create the task.
    :type data: TaskCreate

    :param current_user: The current user who is creating the task.
    :type current_user: User

    :return: The newly created task.
    :rtype: TaskOut
    """
    return await TaskService.create_task(data=data, user=current_user)


@task_router.get('/tasks/{task_id}', summary="Get a task by id", response_model=TaskOut)
async def get_task_by_id(task_id: UUID):
    """
       Get a task by id.

       :param task_id: The id of the task to retrieve.
       :type task_id: :class:`UUID`

       :return: The task with the specified id.
       :rtype: :class:`TaskOut`

    """
    return await TaskService.get_task_by_id(task_id)


@task_router.put('/tasks/{task_id}', summary="Update task by id", response_model=TaskOut)
async def update_task(task_id: UUID, data: TaskUpdate, current_user: User = Depends(get_current_user)):
    """
    Update a task based on task_id.

    :param task_id: The ID of the task to update.
    :param data: The updated task data.
    :param current_user: The current user making the request.
    :return: The updated task.
    """
    task = await TaskService.get_task_by_id(task_id)

    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    if 'due_date' in data.dict():
        if current_user.id != task.created_by or current_user.role != 'admin':
            raise HTTPException(status_code=403,
                                detail="You do not have permission to update the due date of this task")
    return await TaskService.update_task(task_id=task_id, data=data)


@task_router.delete('/tasks/{task_id}', summary="Delete task by id")
async def delete_task(task_id: UUID):
    """
    Delete task by id.

    :param task_id: The ID of the task to be deleted.
    :return: None

    """
    await TaskService.delete_task(task_id=task_id)
    return None


@task_router.get('/assigned/{user_id}', summary="Get tasks assigned to user")
async def get_assigned_tasks(user_id: UUID) -> List[Task]:
    """
    Get tasks assigned to user.

    :param user_id: The unique identifier of the user.
    :type user_id: UUID
    :return: The list of tasks assigned to the user.
    :rtype: List[Task]
    """
    return await TaskService.list_tasks_by_assignee_id(user_id)


@task_router.get('/overdue', summary="Get all overdue tasks")
async def get_all_overdue_tasks() -> List[Task]:
    """
    Get all overdue tasks.

    :return: A list of all overdue tasks.
    :rtype: List[Task]
    """
    return await TaskService.list_all_overdue_tasks()


@task_router.get('/overdue/{assignee_id}', summary="Get all overdue tasks for an assignee")
async def get_overdue_tasks_by_assignee_id(assignee_id: UUID) -> List[Task]:
    """

    Get all overdue tasks for an assignee by assignee ID.

    Parameters:
    - assignee_id (UUID): The identifier of the assignee.

    Returns:
    - List[Task]: A list of overdue tasks associated with the given assignee.

    """
    return await TaskService.list_overdue_tasks_by_assignee(assignee_id)


@task_router.get('/due/{date}', summary="Get tasks by due date")
async def get_tasks_by_due_date(date: datetime) -> List[Task]:
    """

    Get tasks by due date.

    This method is used to retrieve a list of tasks based on their due date.

    Parameters:
    - date (datetime): The due date for which to retrieve tasks.

    Returns:
    - List[Task]: A list of tasks that are due on the specified date.

    """
    return await TaskService.get_tasks_by_due_date(date)


@task_router.get('/due/{date}/{assignee_id}', summary="Get tasks by due date")
async def get_tasks_by_due_date_and_assignee(date: datetime, assignee_id: UUID) -> List[Task]:
    """
    Get tasks by due date and assignee.

    Parameters:
    - date (datetime): The due date of the tasks.
    - assignee_id (UUID): The ID of the assignee.

    Returns:
    - List[Task]: A list of Task objects matching the given due date and assignee ID.
    """
    return await TaskService.get_tasks_by_due_date_and_assignee(date, assignee_id)
