from fastapi import FastAPI
import requests
from routers.health import router as health_router

app = FastAPI()

app.include_router(health_router)