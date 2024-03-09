import secrets
import uuid
from datetime import datetime
from typing import Union
from uuid import UUID

from app.models.user_model import User


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


def validate_date(date: Union[str, datetime]):
    """
    Validate the date.

    Parameters:
        date (Union[str, datetime]): The date to be validated. It can be either a string in the format '%Y-%m-%d' or a datetime object.

    Returns:
        datetime: The validated date as a datetime object.

    Raises:
        ValueError: If the date is a string but is not in the format '%Y-%m-%d'.
        TypeError: If the date is neither a string nor a datetime object.

    """
    if isinstance(date, str):
        try:
            return datetime.strptime(date, "%Y-%m-%d")
        except ValueError:
            raise ValueError(f"Invalid date format: {date}, expected '%Y-%m-%d'")
    elif isinstance(date, datetime):
        return date
    else:
        raise TypeError(f"Invalid date type: {type(date)}, expected string or datetime")


def generate_password_reset_token() -> str:
    """
    Generates a password reset token.

    :return: A string representing the password reset token.
    """
    return secrets.token_hex(16)
