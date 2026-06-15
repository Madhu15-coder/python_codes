from fastapi import FastAPI
from pydantic import BaseModel 

app = FastAPI()
user = 0
class User(BaseModel):
    name: str
    age: int

@app.post("/create_user")
def create_user(user = user):
    return{
        "messege": "user created",
        "data": user
    }
#pydantic 