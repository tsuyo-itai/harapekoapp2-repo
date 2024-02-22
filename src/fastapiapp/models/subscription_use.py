from sqlalchemy import Column, DateTime, Date, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import Integer
from db.database import Base
from datetime import datetime

class SubscriptionUse(Base):
    __tablename__ = 'subscription_uses'
    id = Column(Integer, primary_key=True, index=True)
    used_at = Column(Date)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), default=datetime.utcnow)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    # Subscription とのリレーションシップを定義
    subscription_id = Column(Integer, ForeignKey('subscriptions.id'), index=True, nullable=False)
    subscription = relationship("Subscription", back_populates="subscription_use")

    # Store とのリレーションシップを定義
    store_id = Column(Integer, ForeignKey('stores.id'), index=True, nullable=False)
    store = relationship("Store", back_populates="subscription_use")