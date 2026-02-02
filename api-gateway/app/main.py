from fastapi import FastAPI, Request, Response
import httpx

app = FastAPI(title="API Gateway")

AUTH_SERVICE_URL = "http://localhost:8001"


@app.api_route(
    "/auth/{path:path}",
    methods=["GET", "POST", "PUT", "DELETE", "PATCH"]
)
async def proxy_to_auth(path: str, request: Request):
    url = f"{AUTH_SERVICE_URL}/{path}"

    headers = dict(request.headers)
    body = await request.body()

    async with httpx.AsyncClient() as client:
        auth_response = await client.request(
            method=request.method,
            url=url,
            headers=headers,
            content=body,
            params=request.query_params
        )

    return Response(
        content=auth_response.content,
        status_code=auth_response.status_code,
        headers=dict(auth_response.headers),
    )
