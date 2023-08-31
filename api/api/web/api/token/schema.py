from typing import Optional

from pydantic import BaseModel


class KeyTokenPostDTO(BaseModel):
    """DTO for when generating JWT token."""

    key_token: Optional[str]


class JWTTokenPostDTO(BaseModel):
    """DTO for when responce JWT token."""

    refresh_token: str
