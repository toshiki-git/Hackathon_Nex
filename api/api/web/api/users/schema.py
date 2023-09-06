from pydantic import BaseModel, ConfigDict


class UserModelDTO(BaseModel):
    id: int
    username: str
    email: str
    model_config = ConfigDict(from_attributes=True)
