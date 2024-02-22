from sqlalchemy import Column, Time, Boolean, DateTime, Date, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import Integer
from db.database import Base
from datetime import datetime

class StoreSubscription(Base):
    __tablename__ = 'store_subscriptions'
    id = Column(Integer, primary_key=True, index=True)
    status = Column(Boolean, default=True)
    subscription_start_time = Column(Time)
    subscription_end_time = Column(Time)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), default=datetime.utcnow)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())


    # Store とのリレーションシップを定義
    store_id = Column(Integer, ForeignKey('stores.id'), index=True, nullable=False)
    store = relationship("Store", back_populates="store_subscription")

    # Plan とのリレーションシップを定義
    plan_id = Column(Integer, ForeignKey('plans.id'), index=True, nullable=False)
    plan = relationship("Plan", back_populates="store_subscription")

    # StoreMenu とのリレーションシップを定義
    store_menu = relationship("StoreMenu", back_populates="store_subscription")
