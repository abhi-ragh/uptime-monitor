from fastapi import APIRouter
import requests

router = APIRouter()

@router.get("/healthcheck")
def health(url : str):
    response = requests.get(url)
    return {
        "status": response.status_code
        }