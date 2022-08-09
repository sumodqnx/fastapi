from fastapi import FastAPI
from fastapi.params import Body

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello!!!"}

@app.get("/posts")
def get_posts():
    return {"data": "posts"}

@app.post("/createposts")
def create_posts(payload: dict=Body(...)):
    return {"msg": "created posts"}