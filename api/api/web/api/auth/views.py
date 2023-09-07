from fastapi import APIRouter

from api.web.api.auth import google, logout, jwt

router = APIRouter()
router.include_router(google.router, prefix="/google", tags=["GoogleAuth"])
router.include_router(logout.router, prefix="/logout", tags=["Logout"])
router.include_router(jwt.router, prefix='/jwt_verify', tags=["TMP"])
