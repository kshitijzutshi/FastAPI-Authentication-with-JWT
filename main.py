import uvicorn
from fastapi import FastAPI, Body, Depends
from app.model import PostSchema
from app.model import UserSchema
from app.model import UserLoginSchema
from app.auth.jwt_handler import signJWT
from app.auth.jwt_bearer import JWTBearer


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


#4 Post a new post
# A new post can be posted only if the user is logged in and JWT token is valid
@app.post("/posts", dependencies=[Depends(JWTBearer())], tags=["posts"])
def create_post(post: PostSchema):
    post.id = len(posts) + 1
    posts.append(post.dict())
    print(posts)
    return {
        "message": "Post created successfully"
    }

#5 User Signup
@app.post("/users/signup", tags=["user"])
def user_signup(user: UserSchema = Body(default=None)):
    users.append(user)
    return signJWT(user.email)

def check_user(data: UserLoginSchema):
    for user in users:
        if user.email == data.email and user.password == data.password:
            return True
        return False

# 6 User Login
@app.post("/users/login", tags=["user"])
def user_login(data: UserLoginSchema = Body(default=None)):
    if check_user(data):
        return signJWT(data.email)
    return {"message": "Invalid credentials"}

#7 User list 
@app.get("/users", tags=["users"])
def get_users():
    return {"data": users}