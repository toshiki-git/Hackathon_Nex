from typing import Optional
from pydantic import BaseModel, ConfigDict


class UserModelDTO(BaseModel):
    """DTO for User model."""

    id: int
    username: Optional[str]
    display_name: str
    email: str
    session_cert: Optional[str] = None
    is_initialized: bool
    model_config = ConfigDict(from_attributes=True)

class UpdateUserModelDTO(BaseModel):
    """DTO for update user model."""

    username: Optional[str] = None
    display_name: Optional[str] = None
