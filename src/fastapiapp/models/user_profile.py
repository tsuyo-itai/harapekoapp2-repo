from sqlalchemy import Table, Column, Boolean, DateTime, Date, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import Integer, String
from db.database import Base
from datetime import datetime

class UserProfile(Base):
    __tablename__ = 'user_profiles'
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(50))
    last_name = Column(String(50))
    phone_number = Column(String(24))
    postal_code = Column(String(12))
    prefecture = Column(String(255))
    city = Column(String(255))
    address = Column(String(255))
    date_of_birth = Column(Date)
    icon_image = Column(String(1024))
    created_at = Column(DateTime(timezone=True), server_default=func.now(), default=datetime.utcnow)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    # User とのリレーションシップを定義
    user_id = Column(Integer, ForeignKey('users.id'), index=True, nullable=False)
    user = relationship("User", back_populates="profile")