from typing import Any, Optional
from pydantic import BaseModel, EmailStr


class User(BaseModel):
    telegram_id: int
    token: Optional[dict[str, Any]] = None

    class Config:
        from_attributes = True


class UserCreateDB(BaseModel):
    telegram_id: int
    token: Optional[dict[str, Any]] = None


class UserUpdateDB(BaseModel):
    telegram_id: int
    token: Optional[dict[str, Any]] = None