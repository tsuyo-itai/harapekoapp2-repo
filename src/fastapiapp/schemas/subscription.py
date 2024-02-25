from pydantic import BaseModel
from typing import Optional
from datetime import datetime, date
from schemas.plan import PlanBase


class SubscriptionBase(BaseModel):
    status: bool
    start_date: date
    end_date: date

class SubscriptionCreate(SubscriptionBase):
    pass

class Subscription(SubscriptionBase):
    id: int
    plan_id: Optional[int]
    created_at: datetime
    updated_at: datetime

    class Config:
        # orm_mode = True
        from_attributes = True

class SubscriptionWithPlan(SubscriptionBase):
    plan: Optional[PlanBase]