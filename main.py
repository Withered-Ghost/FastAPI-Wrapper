import httpx
from fastapi import FastAPI, Request, Response
from pydantic import BaseModel, Field

class Wrapper_Body(BaseModel):
    api: int = Field(1, gt=0, lt=3)
    body: dict = {}

vapi_url = "https://api.vapi.ai/assistant"
retellai_url = "https://api.retellai.com/create-agent"

app = FastAPI()

async def call_api(url: str, payload: dict, headers: list):
    async with httpx.AsyncClient() as client:
        res = await client.post(url=url, json=payload, headers=headers)
        # print(res.content, res.status_code, res.headers)
        return res.content, res.status_code

async def create_agent(body: Wrapper_Body, req: Request, res: Response):
    headers = [(k, v) for k, v in req.headers.raw if k == b'authorization' or k == b'content-type']
    # print(headers)
    if body.api == 1:
        content, status = await call_api(vapi_url, body.body, headers)
        return Response(content, status)
    if body.api == 2:
        content, status = await call_api(retellai_url, body.body, headers)
        return Response(content, status)

app.add_api_route("/create", endpoint=create_agent, methods=["POST"])