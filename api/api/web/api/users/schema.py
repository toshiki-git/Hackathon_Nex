from pydantic import BaseModel, ConfigDict


class UserModelDTO(BaseModel):
    """DTO for User model."""

    id: int
    username: str
    email: str
    model_config = ConfigDict(from_attributes=True)
