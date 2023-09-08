
from fastapi import APIRouter, Cookie, Depends, HTTPException, Response, status
from fastapi.responses import JSONResponse
from loguru import logger

from api.db.dao.magic_link_dao import MagicLinkDAO
from api.db.dao.session_dao import SessionDAO
from api.db.dao.user_dao import UserDAO
from api.settings import settings
from api.static import static
from api.web.api.token.schema import JWTTokenPostDTO, MagicLinkPostDTO

router = APIRouter()
logger = logger.bind(task="Token")


@router.post("/token")
async def generate_token(
    magic_link_dto: MagicLinkPostDTO,
    magic_link_dao: MagicLinkDAO = Depends(),
    session_dao: SessionDAO = Depends(),
) -> Response:
    """Generate a JWT token from key_token.

    :param request: Fastapi Request object
    :param token_dto: KeyTokenPostDTO Object
    :param token_dao: TokenDAO object
    :param user_dao: UserDAO object
    :raises NoResultFound: Not found user when expire key_token.
    :returns:
        200_OK: Succeed to generate JWT token
        Invalid key_token: When not found key_token.
        Unauthorized HTTP: When the key_token is expired.
    """
    magic_link = await magic_link_dao.get_magic_link_from_seal(seal=magic_link_dto.seal)

    if magic_link is None:
        logger.error("Not found seal to generate token")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Not found seal to generate token.",
        )

    if magic_link.is_valid():
        magic_link.expire()
        session_info = await session_dao.create_session(user_id=magic_link.user_id)
        response = JSONResponse(session_info)
        response.set_cookie(
            key="access_token",
            value=session_info["access_token"],
            max_age=int(static.ACCESS_TOKEN_EXPIRE_TIME.total_seconds()),
            secure=settings.is_production,
            domain=settings.domain,
            samesite="strict",
            httponly=True,
        )
        response.set_cookie(
            key="session_id",
            value=session_info["session_id"],
            max_age=int(static.REFRESH_TOKEN_EXPIRE_TIME.total_seconds()),
            secure=settings.is_production,
            domain=settings.domain,
            samesite="strict",
            httponly=True,
        )

        return response
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED, detail="Your seal is expired."
    )


@router.post("/token/refresh")
async def generate_jwt_token(
    token_dto: JWTTokenPostDTO,
    user_dao: UserDAO = Depends(),
    session_dao: SessionDAO = Depends(),
    session_id: str = Cookie(default=None),
) -> Response:
    """Function to generate a JWT token from refresh token.

    :param request: Request object of FastAPI
    :param token_dto: JWTTokenPostDTO object
    :param user_dao: UserDAO object
    :returns:
        200: Return new JWT token.
        401: Invalid token or expired token
    """
    if session_id is None and token_dto.session_id:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Not found session_id in the request.",
        )

    session_cert = ""
    if token_dto.session_id is not None:
        session_cert = token_dto.session_id
    elif session_id is not None:
        session_cert = session_id

    session = await session_dao.get_from_session_cert(session_cert)

    if session is not None and session.is_valid():
        user = await user_dao.get_user(user_id=session.user_id)
        new_access_token = session_dao.generate_access_token(user)
        response = JSONResponse({"access_token": new_access_token})
        response.set_cookie(
            key="access_token",
            value=new_access_token,
            max_age=int(static.ACCESS_TOKEN_EXPIRE_TIME.total_seconds()),
            secure=settings.is_production,
            domain=settings.domain,
            samesite="strict",
            httponly=True,
        )

        return response
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED, detail="Expired session_id."
    )


# NOTE: この関数はテスト用関数で、削除予定
@router.get("/test/{user_id}")
async def generate_key_token(  # noqa: D103
    user_id: int,
    magic_link_dao: MagicLinkDAO = Depends(),
) -> str:
    return await magic_link_dao.create_magic_link(user_id=user_id)
