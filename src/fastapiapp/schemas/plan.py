from pydantic import BaseModel
from datetime import datetime


class PlanBase(BaseModel):
    name: str
    price: int
    rank: int

class PlanCreate(PlanBase):
    pass

class PlanUpdate(PlanBase):
    pass

class Plan(PlanBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        # orm_mode = True
        from_attributes = True