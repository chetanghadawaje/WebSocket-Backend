import json

from fastapi import APIRouter, WebSocket
from fastapi.responses import HTMLResponse

from app.utils.api_call import chat_gpt_query

router = APIRouter(
    prefix="/chat",
    tags=["chat"],
    responses={404: {"description": "Not found"}},
)


@router.websocket("/send")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        data = json.loads(data)
        return_data = chat_gpt_query(data)
        await websocket.send_json({"messageReplay": return_data})
