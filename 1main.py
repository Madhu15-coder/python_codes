from fastapi import FastAPI

app = FastAPI()
@app.get("/")


def home():
    return{"message": "Welcome FastAPI"}

@app.get("/about")
def about():
    return{"about":"this website is about ecommerce"}

@app.get("/contact")
def about():
    return{"Contact":"Contact us at support@ecommerce.com"}



