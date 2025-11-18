from fastapi import APIRouter
import httpx,time

import contextlib
from datetime import datetime, timezone
import socket 
import ssl

from urllib.parse import urlparse


def get_ssl_expiry(hostname: str, port: int = 443):
    try:
        context = ssl.create_default_context()

        with contextlib.closing(socket.create_connection((hostname, port), timeout=5)) as sock:
            with contextlib.closing(context.wrap_socket(sock, server_hostname=hostname)) as ssock:
                cert = ssock.getpeercert()
                expiry_str = cert["notAfter"]
                expiry_date = datetime.strptime(expiry_str, "%b %d %H:%M:%S %Y %Z")

        days_left = (expiry_date - datetime.datetime.now(timezone.utc)()).days
        return days_left

    except Exception:
        return None


router = APIRouter()

@router.get("/healthcheck")
async def health(url : str):
    parsed = urlparse(url)
    hostname = parsed.hostname
    port = parsed.port

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
            "redirects": len(response.history),
            "Content Length (in Bytes)": len(response.content),
            "SSL Expiry": get_ssl_expiry(hostname,port)
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