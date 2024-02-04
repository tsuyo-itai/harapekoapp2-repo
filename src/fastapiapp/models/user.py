from sqlalchemy import Table, Column, Boolean, DateTime
from sqlalchemy.sql import func
from sqlalchemy.sql.sqltypes import Integer, String
from db.database import Base
from datetime import datetime


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255))
    password = Column(String(255))
    status = Column(Boolean, default=True)  # ここで status フィールドを追加
    # これserver_defaultはutcになっている。DBのデフォルト時刻を変更する必要がありそう？
    created_at = Column(DateTime(timezone=True), server_default=func.now(), default=datetime.utcnow)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
