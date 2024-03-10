from typing import List
from uuid import UUID

from beanie import Link
from fastapi import APIRouter, Depends

from app.api.deps.user_deps import get_current_user
from app.models.project_model import Project
from app.models.task_model import Task
from app.models.user_model import User
from app.schemas.project_schema import ProjectCreate, ProjectUpdate
from app.services.project_service import ProjectService

project_router = APIRouter()


@project_router.get('/', summary="Get all projects")
async def get_all_projects() -> List[Project]:
    return await ProjectService.list_projects()


@project_router.get('/{project_id}', summary="Get a single project by id")
async def get_project_by_id(project_id: UUID) -> Project:
    return await ProjectService.get_project_by_id(project_id)


@project_router.post('/', summary="Create a new project")
async def create_project(project: ProjectCreate, current_user: User = Depends(get_current_user)) -> Project:
    return await ProjectService.create_project(project, current_user)


@project_router.put('/{project_id}', summary="Update project by id")
async def update_project(project_id: UUID, project: ProjectUpdate, current_user: User = Depends(get_current_user)):
    return await ProjectService.update_project(project_id, project, current_user)


@project_router.delete('/{project_id}', summary="Delete project by id")
async def delete_project(project_id: UUID, current_user: User = Depends(get_current_user)):
    return await ProjectService.delete_project(project_id, current_user)


@project_router.get('/tasks/{project_id}', summary="Get all tasks for a project")
async def get_project_tasks(project_id: UUID) -> List[Link[Task]]:
    project = await ProjectService.get_project_by_id(project_id)
    return project.tasks


@project_router.get('/members/{project_id}', summary="Get all project members")
async def get_project_members(project_id: UUID) -> List[Link[User]]:
    project = await ProjectService.get_project_by_id(project_id)
    return project.project_members
