from datetime import datetime, timedelta
from typing import Union, Any

from jose import jwt
from passlib.context import CryptContext

from app.core.config import settings

password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def create_access_token(subject: Union[str, Any], expires_delta: int = None) -> str:
    """
    Create Access Token

    Generate a JSON Web Token (JWT) access token using the given subject and expiration time.

    :param subject: The subject of the token. It can be a string or any other object.
    :param expires_delta: The expiration time delta in seconds. If not provided, the default expiration time from the
    settings will be used.
    :return: The generated JWT access token as a string.

    """
    if expires_delta is not None:
        expires_delta = datetime.utcnow() + expires_delta
    else:
        expires_delta = datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRATION_MINUTES)

    to_encode = {"exp": expires_delta, "sub": subject}
    encoded_jwt = jwt.encode(to_encode, settings.JWT_SECRET_KEY, algorithm=settings.ALGORITHM)
    return encoded_jwt


def create_refresh_token(subject: Union[str, Any], expires_delta: int = None) -> str:
    """
    Create a refresh token for the given subject.

    :param subject: The subject for which the refresh token is created.
    :type subject: Union[str, Any]
    :param expires_delta: The expiration time delta for the refresh token in seconds.
                          If not provided, the default expiration time from settings will be used.
    :type expires_delta: int, optional
    :return: The encoded refresh token.
    :rtype: str
    """
    if expires_delta is not None:
        expires_delta = datetime.utcnow() + expires_delta
    else:
        expires_delta = datetime.utcnow() + timedelta(minutes=settings.REFRESH_TOKEN_EXPIRATION_MINUTES)

    to_encode = {"exp": expires_delta, "sub": subject}
    encoded_jwt = jwt.encode(to_encode, settings.JWT_REFRESH_SECRET_KEY, algorithm=settings.ALGORITHM)
    return encoded_jwt


def get_password(password: str) -> str:
    """
    Hashes a password using the password_context object.

    :param password: The password to be hashed.
    :type password: str
    :return: The hashed password.
    :rtype: str
    """
    return password_context.hash(password)


def verify_password(password: str, hashed_password: str) -> bool:
    """
    Verifies if a given password matches a hashed password.

    :param password: The password to be verified.
    :param hashed_password: The hashed password to be compared against.

    :return: True if the password matches the hashed password, False otherwise.
    """
    return password_context.verify(password, hashed_password)
