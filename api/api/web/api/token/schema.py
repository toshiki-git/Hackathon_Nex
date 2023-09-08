from typing import Optional

from pydantic import BaseModel


class MagicLinkPostDTO(BaseModel):
    """DTO for when generating JWT token."""

    seal: str


class JWTTokenPostDTO(BaseModel):
    """DTO for when responce JWT token."""

    session_id: Optional[str] = None
