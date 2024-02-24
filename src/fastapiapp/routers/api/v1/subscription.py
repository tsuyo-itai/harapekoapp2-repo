from fastapi import APIRouter, Depends, Request, Response, HTTPException
from sqlalchemy.orm import Session
from cruds import cruds_subscription
from db.database import get_db
from schemas.plan import PlanCreate, Plan, PlanUpdate
from schemas.subscription import SubscriptionCreate, Subscription, SubscriptionWithUserAndPlan
from typing import List


subscription_router = APIRouter(prefix='/api/v1', tags=["Subscription"])

plan_router = APIRouter(prefix='/api/v1', tags=["Plan"])


##* Subscription

@subscription_router.get('/subscriptions', response_model=List[Subscription])
def read_subscriptions(limit: int = 10, db: Session = Depends(get_db)):
    subscriptions = cruds_subscription.get_subscriptions(db, limit=limit)
    return subscriptions

@subscription_router.get('/subscription/{subscription_id}', response_model=SubscriptionWithUserAndPlan)
def read_subscription(subscription_id: int, db: Session = Depends(get_db)):
    db_subscription = cruds_subscription.get_subscription(db, subscription_id=subscription_id)
    if not db_subscription:
        raise HTTPException(status_code=404, detail='Subscription not found')
    return db_subscription

@subscription_router.post('/subscriptions', response_model=SubscriptionCreate)
def create_subscription(subscription: SubscriptionCreate, db: Session = Depends(get_db)):
    return cruds_subscription.create_subscription(db=db, subscription=subscription)



##* Plan

@plan_router.get('/plans', response_model=List[Plan])
def read_plans(limit: int = 10, db: Session = Depends(get_db)):
    plans = cruds_subscription.get_plans(db, limit=limit)
    return plans

@plan_router.get('/plan/{plan_id}', response_model=Plan)
def read_plan(plan_id: int, db: Session = Depends(get_db)):
    db_plan = cruds_subscription.get_plan(db, plan_id=plan_id)
    if not db_plan:
        raise HTTPException(status_code=404, detail='Plan not found')
    return db_plan

@plan_router.post('/plans', response_model=PlanCreate)
def create_plan(plan: PlanCreate, db: Session = Depends(get_db)):
    return cruds_subscription.create_plan(db=db, plan=plan)

@plan_router.put('/plan/{plan_id}', response_model=Plan)
def update_plan(plan_id: int, plan: PlanUpdate, db: Session = Depends(get_db)):
    return cruds_subscription.update_plan(db=db, plan_id=plan_id, plan=plan)