from sqlalchemy import create_engine, false
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from .config import settings

# SQLALCHEMY_DATABASE_URL = 'postgresql://<username>:<password>@<ip-address>/databasename/'
# SQLALCHEMY_DATABASE_URL = f'postgresql://postgres:marcusaurelius@localhost:5432/fastApi'
SQLALCHEMY_DATABASE_URL = f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}'

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


Base = declarative_base()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
        
# Connect To Database  
# while True:
#     try:
#         conn = psycopg2.connect(host='localhost', database='fastApi', user='postgres', password='marcusaurelius', cursor_factory=RealDictCursor)
#         cursor = conn.cursor()
#         print('Database connection was successful')
#         break
#     except Exception as error:
#         print("Connecting to database failed")
#         print(f"error: {error}")
#         time.sleep(5)