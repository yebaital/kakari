from beanie import Document, Indexed
from pydantic import EmailStr


class PasswordReset(Document):
    email: Indexed(EmailStr, unique=True)
    token: str
