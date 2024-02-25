from pydantic import BaseModel
from typing import Optional
from datetime import datetime, date
from schemas.subscription import SubscriptionBase

class UserBase(BaseModel):
    email: str

class UserCreate(UserBase):
    password: str

class UserUpdate(UserBase):
    password: Optional[str] = None

class User(UserBase):
    id: int
    status: bool
    created_at: datetime
    updated_at: datetime

    class Config:
        # orm_mode = True
        from_attributes = True

class UserWithSubscription(User):
    subscription: Optional[SubscriptionBase]

#! TODO UserProfileBaseも継承できないか？
class UserWithProfile(User):
    first_name: str
    last_name: str
    phone_number: str
    postal_code: str
    prefecture: str
    city: str
    address: str
    date_of_birth: Optional[date] = None
    icon_image: str