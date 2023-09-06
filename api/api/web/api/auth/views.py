from fastapi import APIRouter

from api.web.api.auth import google

router = APIRouter()
router.include_router(google.router, prefix="/google", tags=["GoogleAuth"])
