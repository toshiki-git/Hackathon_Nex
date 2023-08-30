from datetime import datetime, timedelta
from typing import Any, Dict

from jose import ExpiredSignatureError, JWTError, jwt

from api.settings import settings


def create_token(data: Dict[str, Any], expires_delta: (timedelta | None) = None) -> str:
    data_encode = data.copy()

    if expires_delta is not None:
        expires = datetime.utcnow() + expires_delta
    else:
        expires = datetime.utcnow() + timedelta(minutes=15)

    data_encode.update({"exp": expires})

    encoded_jwt = jwt.encode(
        data_encode, settings.token_secret_key, algorithm=settings.token_algorithm
    )
    return encoded_jwt


def check_token(token: str) -> (Dict[str, Any] | None):
    try:
        payload = jwt.decode(
            token, settings.token_secret_key, algorithms=[settings.token_algorithm]
        )
        return payload
    except (JWTError, ExpiredSignatureError):
        return None


def is_valid(token: str) -> bool:
    try:
        payload = jwt.decode(
            token, settings.token_secret_key, algorithms=[settings.token_algorithm]
        )
        return True
    except (JWTError, ExpiredSignatureError):
        return False
