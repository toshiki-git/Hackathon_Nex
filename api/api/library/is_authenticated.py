from typing import Optional

from fastapi import Depends, Header, HTTPException, Response
from jose import ExpiredSignatureError, JWTError, jwt

from api.db.dao.user_dao import UserDAO
from api.settings import settings
from api.web.api.users.schema import UserModelDTO


async def is_authenticated(
    response: Response,
    authorization: Optional[str] = Header(default=None),
    user_dao: UserDAO = Depends(),
) -> UserModelDTO:
    if authorization is None:
        raise HTTPException(
            status_code=400,
            detail="Authorization header is missing.",
            headers={"WWW-Authenticate": 'Bearer error="invalid_request"'},
        )

    jwt_token = authorization.rsplit(maxsplit=1)[-1]

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
        return UserModelDTO.model_validate(user)

    raise HTTPException(
        status_code=404,
        detail="Not found user.",
        headers={"WWW-Authenticate": 'Bearer error="not_found_user"'},
    )
