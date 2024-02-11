from pydantic import BaseModel
from typing import Optional
from datetime import datetime, date

class UserProfileBase(BaseModel):
    first_name: str
    last_name: str
    phone_number: str
    postal_code: str
    prefecture: str
    city: str
    address: str
    date_of_birth: Optional[date] = None
    icon_image: str

class UserProfileUpdate(UserProfileBase):
    pass

class UserProfile(UserProfileBase):
    id: int
    created_at: datetime
    updated_at:datetime
    user_id: int

    class Config:
        from_attributes = True

