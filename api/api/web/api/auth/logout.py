from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from loguru import logger

from api.db.dao.session_dao import SessionDAO
from api.library.auth import is_authenticated
from api.library.auth.schema import AuthenticatedUser

router = APIRouter()
logger = logger.bind(task="Logout")


@router.post("/")
async def logout(
    user: AuthenticatedUser = Depends(is_authenticated),
    session_dao: SessionDAO = Depends(),
):
    if user.session_cert is not None:
        session = await session_dao.get_from_session_cert(user.session_cert)
        if session is not None:
            session.discard()

    response = JSONResponse({"detail": "Successfully logout."})
    response.set_cookie(
        key="session_id",
        value="",
        max_age=0,
    )
    response.set_cookie(
        key="access_token",
        value="",
        max_age=0,
    )

    return response
