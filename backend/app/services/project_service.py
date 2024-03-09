from typing import List
from uuid import UUID

from fastapi import HTTPException

from app.models.project_model import Project
from app.models.user_model import User
from app.schemas.project_schema import ProjectCreate, ProjectUpdate


class ProjectService:

    @staticmethod
    async def list_projects() -> List[Project]:
        """
        Retrieve a list of all projects.

        Returns:
            List[Project]: A list of Project objects representing all projects stored in the database.

        """
        return await Project.find_all().to_list()

    @staticmethod
    async def create_project(data: ProjectCreate, user: User) -> Project:
        """
        Create a new project.

        Args:
            data (ProjectCreate): The project data.
            user (User): The user creating the project.

        Returns:
            Project: The created project.
        """
        project = Project(**data.dict(exclude_unset=True), project_owner=user)
        return await project.insert()

    @staticmethod
    async def get_project_by_id(project_id: UUID) -> Project:
        """
        Get project by ID.

        This method retrieves a project based on the provided project ID.

        Parameters:
            project_id (UUID): The ID of the project.

        Returns:
            Project: The project object matching the provided ID.

        """
        return await Project.find_one(project_id=project_id)

    @classmethod
    async def update_project(cls, project_id: UUID, data: ProjectUpdate, current_user: User) -> Project:
        """
        Update a project with the given project ID and data.

        Parameters:
            project_id (UUID): The ID of the project to be updated.
            data (ProjectUpdate): The updated data for the project.
            current_user (User): The user making the request.

        Returns:
            Project: The updated project.

        Raises:
            HTTPException: If the project is not found or if the current user is not the owner of the project or doesn't
            have the "admin" role.
        """
        project = await cls.get_project_by_id(project_id)

        if not project:
            raise HTTPException(status_code=404, detail="Project not found")

        if project.project_owner != current_user or "admin" not in current_user.roles:
            raise HTTPException(
                status_code=403,
                detail="You are not the owner of this project.",
            )

        await project.update({"$set": data.dict(exclude_unset=True)})
        await project.save()
        return project

    @classmethod
    async def delete_project(cls, project_id: UUID, current_user: User) -> None:
        """
        Deletes a project.

        Parameters:
        - project_id (UUID): The ID of the project to be deleted.
        - current_user (User): The user making the request.

        Raises:
        - HTTPException: If the project is not found or if the current user is not the owner of the project or an admin.

        Returns:
        - None
        """
        project = await cls.get_project_by_id(project_id)

        if not project:
            raise HTTPException(status_code=404, detail="Project not found")

        if project.project_owner != current_user or "admin" not in current_user.roles:
            raise HTTPException(
                status_code=403,
                detail="You are not the owner of this project.",
            )

        await project.delete()
