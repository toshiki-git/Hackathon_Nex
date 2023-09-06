from pydantic import BaseModel, ConfigDict

class GameTagDTO(BaseModel):
    
    id  : int
    hashtag : str
    model_config = ConfigDict(from_attributes=True)
