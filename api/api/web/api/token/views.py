from datetime import datetime, timedelta

from fastapi import APIRouter, Depends, Request, Response, status, HTTPException
from fastapi.responses import JSONResponse
from jose import ExpiredSignatureError, JWTError, jwt
from loguru import logger
from sqlalchemy.exc import NoResultFound

from api.db.dao.token_dao import TokenDAO
from api.db.dao.user_dao import UserDAO
from api.library.jwt_token import create_token
from api.settings import settings
from api.static import static
from api.web.api.token.schema import JWTTokenPostDTO, KeyTokenPostDTO

router = APIRouter()
logger = logger.bind(task="Token")


@router.post("/token")
async def generate_token(
    token_dto: KeyTokenPostDTO,
    token_dao: TokenDAO = Depends(),
    user_dao: UserDAO = Depends(),
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
    token_list = await token_dao.get_token(key_token=token_dto.key_token)

    if not token_list:
        logger.error("Not found key_token to generate token")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Not found key_token to generate token.",
        )

    for token in token_list:
        when_token_expire: datetime = token.created_at + static.KEY_TOKEN_EXPIRE_TIME
        if datetime.now(static.TIME_ZONE) < when_token_expire:
            await token_dao.expire_token(token.id)

            user = await user_dao.get_user(token.user_id)
            if user is None:
                logger.critical("Not found user when expire key_token.")
                raise NoResultFound()

            token = create_token(
                data={
                    "token_type": "token",
                    "user_id": user.id,
                    "email": user.email,
                    "username": user.username,
                },
                expires_delta=static.TOKEN_EXPIRE_TIME,
            )
            refresh_token = create_token(
                data={
                    "token_type": "refresh_token",
                    "user_id": user.id,
                },
                expires_delta=static.REFRESH_TOKEN_EXPIRE_TIME,
            )

            response = JSONResponse(
                {
                    "token": token,
                    "refresh_token": refresh_token,
                },
            )
            response.set_cookie(
                key="token",
                value=token,
                expires=int(static.TOKEN_EXPIRE_TIME.total_seconds()),
                secure=settings.is_production,
                domain=settings.domain,
                samesite='strict'
            )
            response.set_cookie(
                key="refresh_token",
                value=refresh_token,
                expires=int(static.REFRESH_TOKEN_EXPIRE_TIME.total_seconds()),
                secure=settings.is_production,
                domain=settings.domain,
                samesite='strict'
            )
            return response

    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED, detail="Your key_token is expired."
    )


@router.post("/token/refresh")
async def generate_jwt_token(
    token_dto: JWTTokenPostDTO,
    user_dao: UserDAO = Depends(),
) -> Response:
    """Function to generate a JWT token from refresh token.

    :param request: Request object of FastAPI
    :param token_dto: JWTTokenPostDTO object
    :param user_dao: UserDAO object
    :returns:
        200: Return new JWT token.
        401: Invalid token or expired token
    """
    try:
        payload = jwt.decode(
            token_dto.refresh_token,
            settings.token_secret_key,
            algorithms=[settings.token_algorithm],
        )
    except ExpiredSignatureError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Your refresh token has expired.",
        )
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid refresh_token."
        )

    if payload["token_type"] == "token":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid refresh_token."
        )

    user = await user_dao.get_user(payload["user_id"])
    if user is not None:
        return JSONResponse(
            {
                "token": create_token(
                    data={
                        "token_type": "token",
                        "user_id": user.id,
                        "email": user.email,
                        "username": user.username,
                    },
                ),
            },
        )

    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Your refresh token is invalid.",
    )


# NOTE: この関数はテスト用関数で、削除予定
@router.get("/test/{user_id}")
async def generate_key_token(  # noqa: D103
    request: Request,
    user_id: int,
    token_dao: TokenDAO = Depends(),
) -> str:
    return await token_dao.create_token(user_id=user_id)
