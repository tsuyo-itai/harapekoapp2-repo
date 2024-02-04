from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class UserModel(BaseModel):
    email: str

class UserCreate(UserModel):
    password: str

class UserUpdate(UserModel):
    password: Optional[str] = None

class UserInDBBase(UserModel):
    id: int
    status: bool
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

class User(UserInDBBase):
    pass

class UserInDB(UserInDBBase):
    password: str