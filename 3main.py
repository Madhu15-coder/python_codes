from fastapi import FastAPI

app = FastAPI()

@app.get("/user")
def get_user(name: str = None):
    
    return{"name": name}