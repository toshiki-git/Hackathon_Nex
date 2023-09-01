from fastapi import  HTTPException, Depends, Header, Response
from jose import ExpiredSignatureError, JWTError, jwt
from api.db.dao.user_dao import UserDAO
from api.settings import settings
from typing import Union


async def jwt_verify(
    jwt_token: Union[str, None] = Header(default=None),
    user_dao: UserDAO = Depends(),
) -> Union[Response,dict]:
    try:
        if jwt_token is None:
            return HTTPException(status_code=401, detail="Authorization header is missing")
        
        payload = jwt.decode(
            jwt_token,
            settings.token_secret_key,
            algorithms=[settings.token_algorithm],
        )
        user_id = payload["user_id"]
        user = user_dao.get_user(user_id) 
        if await user_dao.is_email_exists(email=payload["email"]):
            user = await user_dao.get_user_by_email(email=payload["email"])
            if user:
                response_data = {"user_id": user.id, "is_login": True}
                return response_data
            else:
                raise HTTPException(status_code=401, detail="Unauthorized")
        else:
            raise HTTPException(status_code=401, detail="not found email")
    except ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token has expired")
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")