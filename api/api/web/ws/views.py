from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from typing import Dict, Set
import json
from loguru import logger
logger = logger.bind(task="Token")
router = APIRouter()

# コミュニティごとのWebSocket接続を管理
room_websockets: Dict[int, Set[WebSocket]] = {}

@router.websocket("/{community}")
async def websocket_endpoint(websocket: WebSocket, community: int):
    await websocket.accept()

    if community not in room_websockets:
        room_websockets[community] = set()

    room_websockets[community].add(websocket)

    try:
        while True:
            data = await websocket.receive_text()
            data = json.loads(data)

            userName = data.get("userName", "Unknown User")
            message = data.get("message", "")

            response_data = {
                "community": community,
                "userName": userName,
                "message": message
            }
            for ws in room_websockets.get(community, []):
                logger.info(ws)
                await ws.send_text(json.dumps(response_data))

    except WebSocketDisconnect:
        room_websockets[community].remove(websocket)
        print("WebSocket接続が閉じられました")
        if not room_websockets[community]:
            del room_websockets[community]
