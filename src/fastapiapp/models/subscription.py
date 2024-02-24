from sqlalchemy import Column, Boolean, DateTime, Date, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import Integer
from db.database import Base
from datetime import datetime

class Subscription(Base):
    __tablename__ = 'subscriptions'
    id = Column(Integer, primary_key=True, index=True)
    status = Column(Boolean, default=True)
    start_date = Column(Date)
    end_date = Column(Date)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), default=datetime.utcnow)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    # User とのリレーションシップを定義
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User", back_populates="subscription")

    # Plan とのリレーションシップを定義
    plan_id = Column(Integer, ForeignKey('plans.id'))
    plan = relationship("Plan", back_populates="subscription")

    # SubscriptionUse とのリレーションを定義
    subscription_use = relationship("SubscriptionUse", back_populates="subscription")