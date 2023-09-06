from pydantic import BaseModel, ConfigDict
from typing import Optional, List

class TimelinePostsDTO(BaseModel):

    post_id : int
    user_id: int
    content : str
    image_url : Optional[str]
    hashtags: List[str]
    model_config = ConfigDict(from_attributes=True)
    
class TimelineInputDTO(BaseModel):
    user_id: int
    content : str
    image_url : Optional[str]
    hashtags: List[str]

class TimelineSearchDTO(BaseModel):
    hashtags: List[str]
