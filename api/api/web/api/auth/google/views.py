from typing import Optional
from urllib.parse import urlencode, urljoin

from fastapi import APIRouter, Depends, HTTPException, Request, Response, status
from fastapi.responses import RedirectResponse
from loguru import logger

from api.db.dao.magic_link_dao import MagicLinkDAO
from api.db.dao.user_dao import UserDAO
from api.services.oauth import NotVerifiedEmailError, google
from api.settings import settings

router = APIRouter()
logger = logger.bind(task="GoogleAuth")


@router.get("/login")
async def google_login(request: Request) -> Response:
    """Generate login url and redirect.

    :param request: Request object of fastAPI
    :returns: RedirectResponse for google authentication url
    """
    if (settings.google_client_id is None) or (settings.google_client_secret is None):
        if settings.google_client_id is None:
            logger.critical("Not Found Google client id.")
        if settings.google_client_secret is None:
            logger.critical("Not Found Google client secret.")

        logger.critical("Not found client_id or client_secret for google login.")

        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="client_id or client_secret not found to create URL for Google login.",
        )

    logger.info("Success to generate login url and redirect.")
    return RedirectResponse(
        google.auth_url(
            settings.google_client_id,
            redirect_uri=str(request.url_for("google_callback")),
        ),
    )


@router.get("/callback")
async def google_callback(
    request: Request,
    code: Optional[str] = None,
    user_dao: UserDAO = Depends(),
    magic_link_dao: MagicLinkDAO = Depends(),
) -> Response:
    """Process login response from Google.

    When a login or registration is successful,
    you will be automatically logged in via a URL with query parameters.

    :param request: Request object of fastAPI.
    :param code: String will be use to retrieve access token.
    :param user_dao: UserDAO Object
    :param token_dao: TokenDAO Object
    :raises NotVerifiedEmailError: If not verified email
    :returns:
        Redirect to login url or response
        BadRequest(400) when code is not valid.
    """
    if code is None:
        logger.error("Google login failed")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Google login faild."
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
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to retrieve the access token for Google login.",
        )

    user_info = await google.get_user_info(access_token)
    user_email = user_info["email"]
    user_email_domain = user_email.split("@")[1]

    if not user_info["verified_email"]:
        raise NotVerifiedEmailError(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Your google is not verified email address.",
        )

    user = await user_dao.get_user_by_email(email=user_email)

    if user is not None:
        user_id = user.id
    else:
        user_id = await user_dao.create_user(
            username=user_info["name"],
            email=user_email,
        )
        logger.info("Created new user: xxxx@{0}".format(user_email_domain))

    query = {"seal": await magic_link_dao.create_magic_link(user_id=user_id)}
    return RedirectResponse(
        "{0}?{1}".format(
            urljoin(settings.web_url, "callback"),
            urlencode(query),
        ),
    )
