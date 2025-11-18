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
            "redirects": len(response.history)    
        }
    except httpx.ConnectTimeout:
        return {
            "url": url,
            "status": "Connect Timeout"
        }
    except httpx.ReadTimeout:
        return{
            "url":url,
            "status":"Read Timeout"
        }
    except httpx.ConnectError:
        return{
            "url":url,
            "status":"Connect Error"    
            }    
    except httpx.RequestError as e:
        return{
            "url":url,
            "status":"Request Error",
            "error":str(e)
        }
    except Exception as e:
        return{
            "url":url,
            "status":"down",
            "error":str(e)
        }