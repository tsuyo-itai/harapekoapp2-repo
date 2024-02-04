from sqlalchemy import create_engine, Column, Integer, String, DateTime, MetaData, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
from datetime import datetime

# MySQL接続情報
DATABASE_URL = "mysql+mysqlconnector://root:password@db:3306/develop_harapeko"

# SQLAlchemyエンジンの作成
engine = create_engine(DATABASE_URL)

session = scoped_session(
    sessionmaker(autocommit=False, autoflush=False, bind=engine)
)

Base = declarative_base()

Base.query = session.query_property()

def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()
