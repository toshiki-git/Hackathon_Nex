from typing import Optional
from pydantic import BaseModel, ConfigDict


class UserModelDTO(BaseModel):
    """DTO for User model."""

    id: int
    username: Optional[str]
    display_name: str
    email: str
    session_cert: Optional[str]
    model_config = ConfigDict(from_attributes=True)
