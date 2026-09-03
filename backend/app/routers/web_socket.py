from fastapi import APIRouter, WebSocket

from app.services import ws_chat


router = APIRouter()


@router.websocket("/ws/chat")
async def chat(websocket: WebSocket):
    await ws_chat.ws_endpoint(websocket)
