from fastapi import  HTTPException, Depends, Header, Response
from jose import ExpiredSignatureError, JWTError, jwt
from api.db.dao.user_dao import UserDAO
from api.settings import settings
from api.web.api.auth.jwt.schema import UserModelDTO
from typing import List

async def jwt_verify(
    jwt_token : str = Header(),
    user_dao: UserDAO = Depends(),
) -> UserModelDTO:
    try:
        if jwt_token is None:
            raise  HTTPException(status_code=401, detail="Authorization header is missing")

        payload = jwt.decode(
            jwt_token,
            settings.token_secret_key,
            algorithms=[settings.token_algorithm],
        )
    except ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token has expired")
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")
    
    user = await user_dao.get_user(payload["user_id"])
        
    if  user is not None:
        user_dto = UserModelDTO(id=user.id, display_name=user.display_name, email=user.email)
        return  user_dto
    else:
        raise HTTPException(status_code=401, detail="non existent user")