import uuid
from uuid import UUID


def validate_uuid(id: UUID):
    """
    Validates the provided task ID for
    correct UUID format.

    :param id: The task ID to be validated.
    :raises ValueError: If an invalid task_id is provided.
    """
    try:
        uuid.UUID(id)
    except ValueError:
        raise ValueError("Invalid task id provided.")
