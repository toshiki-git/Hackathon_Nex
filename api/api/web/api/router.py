from fastapi.routing import APIRouter

from api.web.api import auth, docs, dummy, echo, monitoring, redis, timeline, token, users, websocket,community

api_router = APIRouter()
api_router.include_router(monitoring.router)
api_router.include_router(docs.router)
api_router.include_router(token.router, tags=["auth"])
api_router.include_router(auth.router, prefix="/auth", tags=["Auth"])
api_router.include_router(users.router, prefix="/users", tags=["Users"])
api_router.include_router(timeline.router, prefix="/timeline", tags=["timeline"])
api_router.include_router(websocket.router, prefix="/ws", tags=["Websocket"])
api_router.include_router(community.router, prefix="/community", tags=["community"])
api_router.include_router(echo.router, prefix="/echo", tags=["echo"])
api_router.include_router(dummy.router, prefix="/dummy", tags=["dummy"])
api_router.include_router(redis.router, prefix="/redis", tags=["redis"])
