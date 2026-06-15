from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from typing import List
todos = []

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/todos")
def get_todos():
    return todos

class Todo(BaseModel):
    id: int
    title: str
    completed: bool

@app.post("/todos")
def create_todos(todo: Todo):
    todos.append(todo)
    return todo

@app.put("/todos/{todo_id}")
def update_todos(todo_id: int, todo: Todo):
    for Index, Todo in enumerate(todos):
        if Todo.id == todo.id:
            todos[Index] = todo
            return todos[Index]
    return {"message": "todo not found"}

@app.delete("/todos/{todo_id}")
def delete_todos(todo_id: int):
    for Index, Todo in enumerate(todos):
        if Todo.id == todo_id:
            todos.pop(Index)
            return {"message": "todo deleted"}
    return {"message": "todo not found"}


    