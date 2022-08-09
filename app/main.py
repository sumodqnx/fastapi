from fastapi import FastAPI, Response, status, HTTPException
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
from random import randrange

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool=True
    rating: Optional[int] = None

my_posts = [{"title": "title1", "content": "content of post1", "id": 1}, 
            {"title": "title2", "content": "content of post2", "id": 2}
            ]


def find_post(id):
    for p in my_posts:
        if p["id"] == id:
            return p

def find_index_post(id):
    for i, p in enumerate(my_posts):
        if p["id"] == id:
            return i


@app.get("/")
def root():
    return {"message": "Hello!!!"}

@app.get("/posts")
def get_posts():
    return {"data": my_posts}

@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_posts(post: Post):
    p = post.dict()
    p["id"] = randrange(0, 10000000)
    my_posts.append(p)
    return {"data": p}

@app.get("/posts/{id}")
def get_post(id: int, response: Response):
    p = find_post(id)
    if not p:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post {id} not found")
    return {"data detailed": p}

@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
    idx = find_index_post(id)
    if idx == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post {id} not found")
    my_posts.pop(idx)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@app.put("/posts/{id}")
def update_post(id: int, post: Post):
    idx = find_index_post(id)
    if idx == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post {id} not found")
    post_dict = post.dict()
    post_dict['id'] = id
    my_posts[idx] = post_dict
    return {"data": post_dict}