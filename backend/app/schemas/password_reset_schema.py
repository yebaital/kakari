from pydantic import BaseModel


class PasswordResetSchema(BaseModel):
    new_password: str
