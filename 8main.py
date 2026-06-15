from fastapi import FastAPI
from pydantic import BaseModel
todos = []

app = FastAPI()

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





# git init -->>initialize repo

# git add . -->staging area

# git commit -m "message"

# git branch -M main

# git remote add origin __link__

# git push -u origin main

    