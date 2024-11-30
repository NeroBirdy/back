from typing import Any, Optional
from pydantic import BaseModel, EmailStr


class User(BaseModel):
    telegram_id: int
    email: Optional[EmailStr]
    token: Optional[dict[str, Any]]

    class Config:
        from_attributes = True


class UserCreateDB(BaseModel):
    telegram_id: int
    email: Optional[EmailStr]
    token: Optional[dict[str, Any]]


class UserUpdateDB(BaseModel):
    telegram_id: int
    email: Optional[EmailStr]
    token: Optional[dict[str, Any]]