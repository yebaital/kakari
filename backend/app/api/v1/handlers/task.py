from typing import List
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException

from app.api.deps.user_deps import get_current_user
from app.models.task_model import Task
from app.models.user_model import User
from app.schemas.task_schema import TaskOut, TaskCreate, TaskUpdate
from app.services.task_service import TaskService

task_router = APIRouter()


@task_router.get('/', summary="Get all tasks of the user", response_model=List[TaskOut])
async def list_user_tasks(current_user: User = Depends(get_current_user)):
    return await TaskService.list_tasks(current_user)


@task_router.post('create', summary="Create a new task", response_model=TaskOut)
async def create_task(data: TaskCreate, current_user: User = Depends(get_current_user)):
    return await TaskService.create_task(data=data, user=current_user)


@task_router.get('/{task_id}', summary="Get a task by id", response_model=TaskOut)
async def get_task_by_id(task_id: UUID):
    return await TaskService.get_task_by_id(task_id)


@task_router.put('/{task_id}', summary="Update task by id", response_model=TaskOut)
async def update_task(task_id: UUID, data: TaskUpdate, current_user: User = Depends(get_current_user)):
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
    await TaskService.delete_task(task_id=task_id)
    return None
