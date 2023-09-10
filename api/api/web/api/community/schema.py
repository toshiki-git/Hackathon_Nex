from pydantic import BaseModel, ConfigDict


class CommunityDTO(BaseModel):
    user_id: int
    community_id: int
    content: str

