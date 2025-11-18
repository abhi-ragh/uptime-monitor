from fastapi import APIRouter
import httpx,time

router = APIRouter()

@router.get("/healthcheck")
async def health(url : str):
    start = time.perf_counter()
    try:
        async with httpx.AsyncClient(timeout=5.0) as client:
            response = await client.get(url)
        duration = (time.perf_counter() - start) * 1000
        return {
            "url": url,
            "status": "up" if response.status_code < 500 else "down",
            "status_code": response.status_code,
            "response-time": f"{round(duration,2)} ms",
        }
    except Exception as e:
        return{
            "url":url,
            "status":"down",
            "error":e
        }