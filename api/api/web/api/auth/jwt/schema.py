from pydantic import BaseModel, ConfigDict


class UserModelDTO(BaseModel):
    id: int
    display_name: str
    email: str
    model_config = ConfigDict(from_attributes=True)