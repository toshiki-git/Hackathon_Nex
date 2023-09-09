from typing import Optional
from pydantic import BaseModel, ConfigDict


class UserModelDTO(BaseModel):
    """DTO for User model."""

    id: int
    username: str
    email: str
    session_cert: Optional[str] = None
    model_config = ConfigDict(from_attributes=True)
