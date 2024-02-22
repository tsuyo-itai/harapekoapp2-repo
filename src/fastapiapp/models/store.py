from sqlalchemy import Column, String, Text, DateTime, Time, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import Integer
from db.database import Base
from datetime import datetime

class Store(Base):
    __tablename__ = 'stores'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))
    phone_number = Column(String(24))
    postal_code = Column(String(12))
    prefecture = Column(String(255))
    city = Column(String(255))
    address = Column(String(255))
    website = Column(String(255))
    opening_time = Column(Time)
    closing_time = Column(Time)
    category = Column(String(255))
    features = Column(Text)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), default=datetime.utcnow)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    # SubscriptionUse とのリレーションを定義
    subscription_use = relationship("SubscriptionUse", back_populates="store", cascade="all, delete-orphan")

    # StoreMenu とのリレーションを定義
    store_menu = relationship("StoreMenu", back_populates="store", cascade="all, delete-orphan")

    # StoreSubscription とのリレーションを定義
    store_subscription = relationship("StoreSubscription", back_populates="store", cascade="all, delete-orphan")