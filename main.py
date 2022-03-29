import uvicorn
from fastapi import FastAPI
from app.model import PostSchema


# Create dummy posts
posts = [
    {
        "id": 1,
        "title": "Penguins are awesome",
        "text": "They are the most awesome animals ever"
    },
    {
        "id": 2,
        "title": "Tigers are awesome",
        "text": "Wear stripes like a tiger"
    },
    {
        "id": 3,
        "title": "Elephants are awesome",
        "text": "Large Herbivorous Mammals"
    }
]

users = []


app = FastAPI()


#1 Get for testing
@app.get("/", tags=["test"])
def greet():
    return {"message": "Hello World"}

#2 Get posts
@app.get("/posts", tags=["posts"])
def get_posts():
    return {"data": posts}

#3 Get post by id
@app.get("/posts/{id}", tags=["posts"])
def get_post(id: int):
    post = [post for post in posts if post["id"] == id]
    if len(post) == 0:
        return {"message": "No Post not found"}
    elif id > len(posts):
        return {"message": "Post with id {} not found".format(id)}
    return post[0]