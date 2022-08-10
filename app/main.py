from email.policy import HTTP
from fastapi import FastAPI, Response, status, HTTPException, Depends
from fastapi.params import Body
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from . import models, schemas, utils
from .database import engine, SessionLocal, get_db
from sqlalchemy.orm import Session
from .routers import post, user



models.Base.metadata.create_all(bind=engine)
app = FastAPI()


while True:
    try:
        conn = psycopg2.connect(host="localhost", database="fastapi", user="postgres", 
        password=" ", cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print("Successively connect to db")
        break
    except Exception as e:
        print("Failed to connect to db")
        print("error:", e)
        time.sleep(2)

app.include_router(post.router)
app.include_router(user.router)


@app.get("/")
def root():
    return {"message": "Hello!!!"}




