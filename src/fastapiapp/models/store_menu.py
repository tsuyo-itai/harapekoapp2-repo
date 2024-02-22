from sqlalchemy import Column, String, DateTime, Date, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import Integer
from db.database import Base
from datetime import datetime

class StoreMenu(Base):
    __tablename__ = 'store_menus'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))
    description = Column(String(255))
    price = Column(Integer)
    image = Column(String(255))
    created_at = Column(DateTime(timezone=True), server_default=func.now(), default=datetime.utcnow)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    # Store とのリレーションシップを定義
    store_id = Column(Integer, ForeignKey('stores.id'), index=True, nullable=False)
    store = relationship("Store", back_populates="store_menu")

    # StoreSubscription とのリレーションシップを定義
    store_subscription_id = Column(Integer, ForeignKey('store_subscriptions.id'), index=True, nullable=False)
    store_subscription = relationship("StoreSubscription", back_populates="store_menu")