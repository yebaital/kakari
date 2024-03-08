from typing import List
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException

from app.api.deps.user_deps import get_current_user
from app.models.user_model import User
from app.schemas.task_schema import TaskOut, TaskCreate, TaskUpdate
from app.services.task_service import TaskService

task_router = APIRouter()


@task_router.get('/', summary="Get all tasks of the user", response_model=List[TaskOut])
async def list_user_tasks(current_user: User = Depends(get_current_user)):
    """
    Get all tasks of the user

    :param current_user: The current user
    :return: A list of tasks for the user
    :rtype: List[TaskOut]
    """
    return await TaskService.list_tasks(current_user)


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


@task_router.get('/{task_id}', summary="Get a task by id", response_model=TaskOut)
async def get_task_by_id(task_id: UUID):
    """
       Get a task by id.

       :param task_id: The id of the task to retrieve.
       :type task_id: :class:`UUID`

       :return: The task with the specified id.
       :rtype: :class:`TaskOut`

    """
    return await TaskService.get_task_by_id(task_id)


@task_router.put('/{task_id}', summary="Update task by id", response_model=TaskOut)
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


@task_router.delete('/{task_id}', summary="Delete task by id")
async def delete_task(task_id: UUID):
    """
    Delete task by id.

    :param task_id: The ID of the task to be deleted.
    :return: None

    """
    await TaskService.delete_task(task_id=task_id)
    return None

# TODO: add endpoint to get tasks by user
# TODO: add endpoint to get overdue tasks
# TODO: add endpoint to get tasks by due date
