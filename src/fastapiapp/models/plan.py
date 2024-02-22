from sqlalchemy import Column, String, DateTime, Date, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import Integer
from db.database import Base
from datetime import datetime

class Plan(Base):
    __tablename__ = 'plans'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))
    price = Column(Integer)
    rank = Column(Integer)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), default=datetime.utcnow)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    # Subscription とのリレーションシップを定義
    subscription = relationship("Subscription", back_populates="plan")

    # StoreSubscription とのリレーションを定義
    store_subscription = relationship("StoreSubscription", back_populates="plan")