from sqlalchemy import create_engine, Column, Integer, String, DateTime, MetaData, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
from datetime import datetime
import os

# MySQL接続情報
user_name = os.environ.get('DB_USERNAME')
password = os.environ.get('DB_PASSWORD')
host = os.environ.get('DB_HOST')
database_name = os.environ.get('DB_DATABASE')

DATABASE_URL = f'mysql+mysqlconnector://{user_name}:{password}@{host}:3306/{database_name}'

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
