from pydantic import BaseModel, ConfigDict
from typing import Optional

class TimelinePostsSchema(BaseModel):

    user_id: int
    content : str
    image_url : Optional[str]
    model_config = ConfigDict(from_attributes=True)

