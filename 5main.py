from fastapi import FastAPI

app = FastAPI()

@app.post("/create_user")
def create_user(name: str, age: int):
    return{
        "message": "User created",
        "data": {
            "name":name,
            "age": age
        }
    }
