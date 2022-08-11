from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
# import psycopg2
# from psycopg2.extras import RealDictCursor
# import time

SQLALCHEMY_DATABASE_URL = 'postgresql://postgres: @localhost/fastapi'
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

# while True:
#     try:
#         conn = psycopg2.connect(host="localhost", database="fastapi", user="postgres", 
#         password=" ", cursor_factory=RealDictCursor)
#         cursor = conn.cursor()
#         print("Successively connect to db")
#         break
#     except Exception as e:
#         print("Failed to connect to db")
#         print("error:", e)
#         time.sleep(2)