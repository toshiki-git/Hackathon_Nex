from typing import Optional

from pydantic import BaseModel, ConfigDict


class TimelinePostsDTO(BaseModel):

    user_id: int
    content: str
    image_url: Optional[str]
    model_config = ConfigDict(from_attributes=True)
