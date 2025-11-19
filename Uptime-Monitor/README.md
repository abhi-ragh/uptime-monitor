# Uptime Monitor

Uptime Monitor is a FastAPI-based web service that provides tools to monitor the health of a given URL.

## Features

*   **Health Check**: Get the health status of a URL, including status code, response time, and SSL certificate expiry.
*   **IP Lookup**: Get the IP address of a given URL.
*   **Header Inspection**: Get the HTTP headers of a given URL.

## Endpoints

### GET /healthcheck

This endpoint checks the health of a given URL.

**Query Parameter:**

*   `url` (HttpUrl): The URL to check.

**Example Request:**

```
GET /healthcheck?url=https://www.google.com
```

**Example Response:**

```json
{
    "url": "https://www.google.com/",
    "status": "up",
    "status_code": 200,
    "status_category": "Success",
    "response-time": "153.33 ms",
    "redirects": 0,
    "Content Length (in Bytes)": 14310,
    "redirect_to": null,
    "SSL Expiry": 69
}
```

### GET /ip

This endpoint returns the IP address of a given URL.

**Query Parameter:**

*   `url` (HttpUrl): The URL to get the IP address of.

**Example Request:**

```
GET /ip?url=https://www.google.com
```

**Example Response:**

```json
{
    "ip_address": "142.250.190.78"
}
```

### GET /headers

This endpoint returns the HTTP headers of a given URL.

**Query Parameter:**

*   `url` (HttpUrl): The URL to get the headers of.

**Example Request:**

```
GET /headers?url=https://www.google.com
```

**Example Response:**

```json
{
    "headers": {
        "date": "Tue, 18 Nov 2025 15:00:00 GMT",
        "expires": "-1",
        "cache-control": "private, max-age=0",
        "content-type": "text/html; charset=ISO-8859-1",
        "p3p": "CP=\"This is not a P3P policy! See g.co/p3phelp for more info.\"",
        "server": "gws",
        "x-xss-protection": "0",
        "x-frame-options": "SAMEORIGIN",
        "set-cookie": "1P_JAR=2025-11-18-15; expires=Thu, 18-Dec-2025 15:00:00 GMT; path=/; domain=.google.com; Secure, AEC=Ackid1Q...; expires=Sun, 17-May-2026 15:00:00 GMT; path=/; domain=.google.com; Secure; HttpOnly; SameSite=lax",
        "alt-svc": "h3=\":443\"; ma=2592000,h3-29=\":443\"; ma=2592000",
        "transfer-encoding": "chunked"
    }
}
```

