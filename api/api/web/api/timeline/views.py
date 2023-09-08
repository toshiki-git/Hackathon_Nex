from fastapi import APIRouter

from api.web.api.timeline import public

router = APIRouter()
router.include_router(public.router, prefix="/public", tags=["Public Timeline"])
