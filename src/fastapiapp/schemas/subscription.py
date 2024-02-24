from pydantic import BaseModel
from typing import Optional
from datetime import datetime, date
from schemas.user import UserBase
from schemas.plan import PlanBase


class SubscriptionBase(BaseModel):
    status: bool
    start_date: date
    end_date: date

class SubscriptionCreate(SubscriptionBase):
    pass

class Subscription(SubscriptionBase):
    id: int
    user_id: Optional[int]
    plan_id: Optional[int]
    created_at: datetime
    updated_at: datetime

    class Config:
        # orm_mode = True
        from_attributes = True

class SubscriptionWithUser(SubscriptionBase):
    user: Optional[UserBase]

class SubscriptionWithPlan(SubscriptionBase):
    plan: Optional[PlanBase]

class SubscriptionWithUserAndPlan(SubscriptionBase):
    user: Optional[UserBase]
    plan: Optional[PlanBase]