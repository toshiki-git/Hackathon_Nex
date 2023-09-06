from pydantic import BaseModel, ConfigDict
from typing import Optional, List

class TimelinePostsDTO(BaseModel):

    user_id: int
    content : str
    image_url : Optional[str]
    game_ids: List[int]
    model_config = ConfigDict(from_attributes=True)
    
class TimelineInputDTO(BaseModel):
    user_id: int
    content : str
    image_url : Optional[str]
    game_titles: List[str]
