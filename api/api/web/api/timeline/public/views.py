from typing import List

from fastapi import APIRouter
from fastapi.param_functions import Depends

from api.db.models.timeline_posts_model import TimelinePostsModel
from api.db.dao.timeline_posts import TimelinePostsDAO
from api.web.api.timeline.public.schema import TimelinePostsDTO, TimelineInputDTO
from api.db.dao.hashtag import HashTagDAO

router = APIRouter()

@router.get("/get", response_model=List[TimelinePostsDTO])
async def get_timeline_posts(
    limit: int = 10,
    offset: int = 0,
    timeline_dao: TimelinePostsDAO = Depends(),
    ) -> List[TimelinePostsModel] :
 
    return await timeline_dao.get_timeline_posts(limit=limit, offset=offset)

@router.post("/psot")
async def create_timeline_post(
    new_timeline_object: TimelineInputDTO,
    hashtag_dao : HashTagDAO = Depends (),
    timeline_dao: TimelinePostsDAO = Depends(),
) -> None:
    
    hashtag_data = await hashtag_dao.get_hashtags_exact_by_titles(hashtags=new_timeline_object.hashtags)
    hashtags = [data.hashtag for data in hashtag_data]
    
    #if not hashtags:
        #hashtags=[10]
    
    await timeline_dao.create_timeline_posts(
        user_id = new_timeline_object.user_id,
        content = new_timeline_object.content,
        image_url = new_timeline_object.image_url,
        hashtags = hashtags
    )
    
@router.get("/search", response_model=List[TimelinePostsDTO])
async def get_timeline_tag(
    game_id : int,
    timeline_dao: TimelinePostsDAO = Depends()
) -> List[TimelinePostsModel] :

    return await timeline_dao.get_timeline_tag(game_id=game_id)