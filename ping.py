from fastapi import FastAPI
import requests

app = FastAPI()

@app.get("/healthcheck")
def check(url: str):
    
    status = requests.get(url)

    return{
        "url" : url,
        "Status" : status.status_code
    }