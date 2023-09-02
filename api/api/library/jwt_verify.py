from fastapi import  HTTPException, Depends, Header, Response
from jose import ExpiredSignatureError, JWTError, jwt
from api.db.dao.user_dao import UserDAO
from api.settings import settings


async def jwt_verify(
    jwt_token : str = Header(),
    user_dao: UserDAO = Depends(),
) -> dict[str, int | str]:
    try:
        if jwt_token is None:
            raise  HTTPException(status_code=401, detail="Authorization header is missing")

        payload = jwt.decode(
            jwt_token,
            settings.token_secret_key,
            algorithms=[settings.token_algorithm],
        )
        user_id = payload["user_id"]
        user = await user_dao.get_user(payload["user_id"])
        
        if  user is None:
            raise HTTPException(status_code=401, detail="non existent user")
        
        if await user_dao.is_email_exists(email=payload["email"]):
            user = await user_dao.get_user_by_email(email=payload["email"])
            if user:
                return {"user_id": user.id}

        else:
            raise HTTPException(status_code=401, detail="not found email")
    except ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token has expired")
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")
    
    return  {"user_id": "user.id"}