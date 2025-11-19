from fastapi import APIRouter
from pydantic import BaseModel
import sqlite3 as sql

def get_conn():
    conn = sql.connect('todo.db')
    conn.row_factory = sql.Row
    return conn

def init_db():
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            task TEXT, 
            status TEXT)
    ''')
    conn.commit()
    conn.close()
init_db()

todo = APIRouter()

@todo.get("/")
def read_tasks():
    conn = get_conn()
    cursor = conn.cursor()
    tasks = cursor.execute("SELECT * FROM tasks").fetchall()
    conn.commit()
    conn.close()
    return{
        task['id'] : {
            "task": task["task"],
            "status": task["status"]
        } for task in tasks
    }

@todo.post("/")
def create_task(task: str):
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tasks ('task','status') VALUES (?,?)",(task,"PENDING"))
    conn.commit()
    conn.close()
    return{
        "Status":"Task Created"
    }

@todo.patch("/")
def update_task(id: int, status: str):
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("UPDATE tasks SET status=? WHERE id=?",(status,id))
    conn.commit()
    conn.close()
    return {
        "Status":"Task Updated"
    }