from typing import Optional

from fastapi import APIRouter, Request, status
from fastapi.responses import JSONResponse, RedirectResponse
from loguru import logger

from api.services.oauth import google
from api.settings import settings
from api.utils import json_err_content

router = APIRouter()
logger = logger.bind(task="GoogleAuth")


@router.get("/login")
async def google_login(request: Request) -> RedirectResponse | JSONResponse:
    """Generate login url and redirect.

    :param request: Request object of fastAPI
    :returns: RedirectResponse for google authentication url
    """
    if (settings.google_client_id is None) or (settings.google_client_secret is None):
        if settings.google_client_id is None:
            logger.critical("Not Found Google client id.")
        if settings.google_client_secret is None:
            logger.critical("Not Found Google client secret.")

        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content=json_err_content(
                500,
                "Internal Server Error",
                "client_id or client_secret not found to create URL for Google login.",
            ),
        )

    logger.info("Success to generate login url and redirect.")
    return RedirectResponse(
        google.auth_url(
            settings.google_client_id,
            redirect_uri=str(request.url_for("google_callback")),
        ),
    )


@router.get("/callback")
async def google_callback(request: Request, code: Optional[str] = None) -> JSONResponse:
    """Process login response from Google and return user info.

    :param request: Request object of fastAPI.
    :param code: String will be use to retrieve access token.
    :returns: Returns user info or BadRequest(400) when code is not valid.
    """
    if code is None:
        logger.error("Google login failed")
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content=json_err_content(400, "Bad Request", "Google login faild."),
        )

    try:
        access_token = await google.get_token(
            code=code,
            client_id=settings.google_client_id,
            client_secret=settings.google_client_secret,
            redirect_uri=str(request.url_for("google_callback")),
        )
        logger.info("Success to retrieve access token from Google API.")
    except google.FaildRetrieveAccessTokenError:
        logger.error("Failed to retrieve access token for Google login.")
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content=json_err_content(
                400,
                "Bad Request",
                "Failed to retrieve the access token for Google login.",
            ),
        )

    return JSONResponse(await google.get_user_info(access_token))
