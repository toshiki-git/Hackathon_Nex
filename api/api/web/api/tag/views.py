from typing import List

from fastapi import APIRouter,HTTPException
from fastapi.param_functions import Depends

from api.db.dao.hashtag import HashTagDAO
from api.db.models.hashtag_model import HashTagModel
from api.web.api.tag.schema import GameTagDTO

router = APIRouter()

@router.post("/add_hashtag")
async def create_hashtag(
    hashtag: str,
    hashtag_dao: HashTagDAO = Depends(),
) -> None:

    return await hashtag_dao.create_hashtag(hashtag=hashtag)
    

@router.get("/gain_hashtags", response_model=List[GameTagDTO])
async def get_hashtags(
    limit: int = 10,
    offset: int = 0,
    hashtag_dao: HashTagDAO = Depends(),
) -> List[HashTagModel]:

    hashtag = await hashtag_dao.get_hashtags(limit=limit, offset=offset)
    return hashtag

@router.get("/gain_hashtag_byid", response_model=GameTagDTO)
async def get_hashtag_by_id(
    tag_id: int,
    hashtag_dao: HashTagDAO = Depends(),
) -> HashTagModel:

    hashtag = await hashtag_dao.get_hashtag_by_id(tag_id=tag_id)
    if hashtag is None:
        raise HTTPException(status_code=401, detail="Game tag not found")
    return hashtag



@router.get("/gain_hashtag_bytitle", response_model=List[GameTagDTO])
async def get_tag_partial_by_title(
    hashtag: str,
    hashtag_dao: HashTagDAO = Depends(),
) -> List[HashTagModel]:

    hashtags = await hashtag_dao.get_hashtags_partial_by_title(hashtag=hashtag)
    return hashtags