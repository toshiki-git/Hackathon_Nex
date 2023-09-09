from typing import Optional

from fastapi import Cookie, Depends, Header, HTTPException
from jose import ExpiredSignatureError, JWTError, jwt

from api.db.dao.user_dao import UserDAO

from api.settings import settings
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from api.web.api.users.schema import UserModelDTO

async def is_authenticated(
    user_dao: UserDAO = Depends(),
    access_token: str = Cookie(default=None),
    session_id: str = Cookie(default=None),
    authorization: Optional[str] = Header(default=None),
) -> "UserModelDTO":
    from api.web.api.users.schema import UserModelDTO
    """Autheticates a user based on the provided authorization token.

    This function validates the provided authorization token by decofing it
    and verifying its autheticity. If the token is valid, it retrieves the
    associated user information from the database and returns it as a
    UserModelDTO object.

    :param authorization:
        The authorization token provided in the HTTP headers.
        It should be in the format "Bearer <token>".
    :param user_dao: UserDAO object
    :returns: UserModelDTO object
    :raises HTTPException:
        - 400 (Bad Request): If the authorization header is missing.
        - 401 (Unauthorized): If the token is expired or invalid.
        - 404 (Not Found): If the user associated with the token is not found.
    """
    if authorization is None and access_token is None:
        raise HTTPException(
            status_code=401,
            detail="Authorization credentials is missing.",
            headers={"WWW-Authenticate": 'Bearer error="invalid_request"'},
        )

    if authorization is not None:
        jwt_token = authorization.rsplit(maxsplit=1)[-1]
    else:
        jwt_token = access_token

    try:
        payload = jwt.decode(
            jwt_token,
            settings.token_secret_key,
            algorithms=[settings.token_algorithm],
        )
    except ExpiredSignatureError:
        raise HTTPException(
            status_code=401,
            detail="Token has expired.",
            headers={"WWW-Authenticate": 'Bearer error="invalid_token"'},
        )
    except JWTError:
        raise HTTPException(
            status_code=401,
            detail="Invalid token.",
            headers={"WWW-Authenticate": 'Bearer error="invalid_token"'},
        )

    user = await user_dao.get_user(payload["user_id"])

    if user is not None:
        authenticated_user = UserModelDTO.model_validate(user)
        if session_id is not None:
            authenticated_user.session_cert = session_id
        return authenticated_user

    raise HTTPException(
        status_code=404,
        detail="Not found user.",
        headers={"WWW-Authenticate": 'Bearer error="not_found_user"'},
    )
