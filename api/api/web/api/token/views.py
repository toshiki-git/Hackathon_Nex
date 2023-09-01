from datetime import datetime, timedelta

from jose import ExpiredSignatureError, JWTError, jwt

from api.settings import settings

from fastapi import APIRouter, Depends, Request, Response, status
from fastapi.responses import JSONResponse
from sqlalchemy.exc import NoResultFound
from loguru import logger

from api.db.dao.token_dao import TokenDAO
from api.db.dao.user_dao import UserDAO
from api.static import static
from api.lib.jwt_token import create_token
from api.utils.response import json_err_content
from api.web.api.token.schema import JWTTokenPostDTO, KeyTokenPostDTO

router = APIRouter()
logger = logger.bind(task="Token")


@router.post("/token")
async def generate_token(
    request: Request,
    toke_dto: KeyTokenPostDTO,
    token_dao: TokenDAO = Depends(),
    user_dao: UserDAO = Depends(),
) -> Response:
    """Generate a JWT token from key_token.

    :param request: Fastapi Request object
    :param key_token: key_token to generate JWT token
    :param token_dao: TokenDAO object
    :returns:
        200_OK: Succeed to generate JWT token
        Invalid key_token: When not found key_token.
        Unauthorized HTTP: When the key_token is expired.
    """

    def not_found_key_token() -> Response:  # noqa: WPS430
        logger.error("Not found key_token to generate token")
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content=json_err_content(
                500,
                "Invalid key_token",
                "Not found key_token to generate token.",
            ),
        )

    if toke_dto.key_token is None:
        return not_found_key_token()

    token_list = await token_dao.get_token(key_token=toke_dto.key_token)

    if not token_list:
        return not_found_key_token()

    for token in token_list:
        when_token_expire: datetime = token.created_at + static.KEY_TOKEN_EXPIRE_TIME
        if datetime.now(static.TIME_ZONE) < when_token_expire:
            await token_dao.expire_token(token.id)

            user = await user_dao.get_user(token.user_id)

            if user is None:
                logger.critical("Not found user when expire key_token.")
                raise NoResultFound()

            return JSONResponse(
                {
                    "token": create_token(
                        data={
                            "token_type": "normal",
                            "user_id": user.id,
                            "email": user.email,
                            "username": user.username,
                        },
                    ),
                    "refresh_token": create_token(
                        data={
                            "token_type": "refresh_token",
                            "user_id": user.id,
                        },
                        expires_delta=timedelta(days=90),
                    ),
                },
            )

    return JSONResponse(
        status_code=status.HTTP_401_UNAUTHORIZED,
        content=json_err_content(
            401,
            "Unauthorized HTTP",
            "Your key_token is expired.",
        ),
    )


# TODO: Tokenのリフレッシュ機能をここの関数にて定義
@router.post("/token/refresh")
async def generate_jwt_token(
    request: Request,
    token_dto: JWTTokenPostDTO,
    user_dao: UserDAO = Depends(),
) -> dict:
    """Function to generate a JWT token from refresh token.
    :param request: Request object of FastAPI
    :param token_dto: JWTTokenPostDTO object
    """
    try:
        payload = jwt.decode(
            token_dto.refresh_token,
            settings.token_secret_key,
            algorithms=[settings.token_algorithm],
        )
        
        if payload["token_type"] == "normal":
            return JSONResponse(
                status_code=status.HTTP_401_UNAUTHORIZED,
                content=json_err_content(
                    401,
                    "Invalid token",
                    "This is a normal token"
                )
            )
        
        user = await user_dao.get_user(payload["user_id"])
        if user is not None:          
            return JSONResponse(
                {
                    "token": create_token(
                        data={
                            "token_type": "normal",
                            "user_id": user.id,
                            "email": user.email,
                            "username": user.username,
                        }
                    )
                }
            )
        else:
            return JSONResponse(
                status_code=status.HTTP_401_UNAUTHORIZED,
                content=json_err_content(
                    401,
                    "Invalid user_id",
                    "Your refresh token is invalid",
                ),
        )
    except ExpiredSignatureError:
        return JSONResponse(
            status_code=status.HTTP_401_UNAUTHORIZED,
            content=json_err_content(
                401,
                "Token has expired",
                "Your refresh token has expired",
            ),
        )
    except JWTError:
        return JSONResponse(
            status_code=status.HTTP_401_UNAUTHORIZED,
            content=json_err_content(
                401,
                "Invalid token",
                "Your refresh token is invalid",
            ),
        )



# NOTE: この関数はテスト用関数で、削除予定
@router.get("/test/{user_id}")
async def generate_key_token(
    request: Request,
    user_id: int,
    token_dao: TokenDAO = Depends(),
) -> str:  # noqa: D103
    return await token_dao.create_token(user_id=user_id)
