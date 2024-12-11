from datetime import datetime
from typing import Optional

from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    email: EmailStr
    created_at: Optional[datetime] = datetime.now()
    updated_at: Optional[datetime] = datetime.now()
    is_active: Optional[bool] = True
    is_admin: Optional[bool] = False
    is_delete: Optional[bool] = False


class UserCreate(UserBase):
    name: str
    password: str


class UserLogin(UserBase):
    password: str


class UserResponse(UserBase):
    token: str
    pass
