from sqlalchemy.orm import Session, joinedload

from models import Plan, Subscription
from schemas.plan import PlanCreate, PlanUpdate
from schemas.subscription import SubscriptionCreate


##* Subscription 

def get_subscriptions(db: Session, limit: int = 10):
    return db.query(Subscription).limit(limit).all()

def get_subscription(db: Session, subscription_id: int):
    #! TODO user_idやplan_idがNULLのときもあり得る
    return db.query(Subscription) \
        .options(joinedload(Subscription.user, innerjoin=False), joinedload(Subscription.plan, innerjoin=False)) \
        .filter(Subscription.id == subscription_id) \
        .first()

def create_subscription(db: Session, subscription: SubscriptionCreate):
    db_subscription = Subscription(status=subscription.status,
                                   start_date=subscription.start_date,
                                   end_date=subscription.end_date,
                                   )
    db.add(db_subscription)
    db.commit()
    db.refresh(db_subscription)

    return db_subscription




##* Plan
def get_plans(db: Session, limit: int = 10):
    return db.query(Plan).limit(limit).all()

def get_plan(db: Session, plan_id: int):
    return db.query(Plan).filter(Plan.id == plan_id).first()

def create_plan(db: Session, plan: PlanCreate):
    db_plan = Plan(name=plan.name, price=plan.price, rank=plan.rank)
    db.add(db_plan)
    db.commit()
    db.refresh(db_plan)

    return db_plan

def update_plan(db: Session, plan_id: int, plan: PlanUpdate):
    db_plan = db.query(Plan).filter(Plan.id == plan_id).first()
    db_plan.name = plan.name
    db_plan.price = plan.price
    db_plan.rank = plan.rank
    db.commit()
    return db_plan

def delete_plan(db: Session, plan_id: int):
    db_plan = db.query(Plan).filter(Plan.id == plan_id).first()
    db.delete(db_plan)
    db.commit()