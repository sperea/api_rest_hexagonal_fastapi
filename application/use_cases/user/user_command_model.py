from pydantic import BaseModel, Field, validator
import re


class UserCreateModel(BaseModel):
    """UserCreateModel represents a write model to create a user."""

    username: str = Field(example="testusername")
    password: str = Field(example="testusername")
    email: str = Field(example="testusername@domain.com")


class UserUpdateModel(BaseModel):
    """UserUpdateModel represents a write model to update a user."""

    username: str = Field(example="testusername")
    password: str = Field(example="testusername")
    email: str = Field(example="testusername@domain.com")


    @validator("email")
    def _validate_email(cls, value, **kwargs):
        """Returns True if the email property is a valid email address, False otherwise."""
        pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        if not (bool(re.match(pattern, self.email))):
            raise ValueError(
                "Formato de email no válido.")
        else:
            return value
