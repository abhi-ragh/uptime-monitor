from fastapi import FastAPI
from routers.todo import todo as todo_router

app = FastAPI()

app.include_router(todo_router)