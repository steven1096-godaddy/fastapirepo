from typing import Union

from fastapi import FastAPI
from fastapi.responses import JSONResponse
import requests

app = FastAPI()
SERVICEURL = "https://jsonplaceholder.typicode.com"

@app.get("/")
def read_root():
    return {"Hello": "There"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.get("/api/v1/users")
async def get_users():
    response = requests.get(f"{SERVICEURL}/users")
    if response.status_code == 200:
        users = response.json()
    else:
        print(f"Error: Unable to fetch data. Status code: {response.status_code}")
    return JSONResponse(content=users)

@app.get("/api/v1/users/{user_id}")
async def get_user(user_id: int):
    url = f"{SERVICEURL}/users/{user_id}"
    print(f"URL: {url}")
    response = requests.get(url)
    if response.status_code == 200:
        user = response.json()
    else:
        print(f"Error: Unable to fetch data. Status code: {response.status_code}")
    return JSONResponse(content=user)

@app.get("/api/v1/posts")
async def get_users():
    response = requests.get(f"{SERVICEURL}/posts")
    if response.status_code == 200:
        posts = response.json()
    else:
        print(f"Error: Unable to fetch data. Status code: {response.status_code}")
    return JSONResponse(content=posts)

@app.get("/api/v1/posts/{post_id}")
async def get_user(post_id: int):
    url = f"{SERVICEURL}/posts/{post_id}"
    print(f"URL: {url}")
    response = requests.get(url)
    if response.status_code == 200:
        post = response.json()
    else:
        print(f"Error: Unable to fetch data. Status code: {response.status_code}")
    return JSONResponse(content=post)
