from fastapi.routing import APIRouter

from api.web.ws.views import router
ws_router = APIRouter()


ws_router.include_router(router, tags=["Websocket"])
