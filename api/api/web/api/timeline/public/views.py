from typing import List

from fastapi import APIRouter, Query
from fastapi.param_functions import Depends

from api.db.models.timeline_posts_model import TimelinePostsModel
from api.db.dao.timeline_posts import TimelinePostsDAO
from api.web.api.timeline.public.schema import TimelinePostsDTO, TimelineInputDTO

router = APIRouter()

@router.get("/gain", response_model=List[TimelinePostsDTO])
async def get_timeline_posts(
    limit: int = 10,
    offset: int = 0,
    timeline_dao: TimelinePostsDAO = Depends(),
    ) -> List[TimelinePostsModel] :
 
    return await timeline_dao.get_timeline_posts(limit=limit, offset=offset)

@router.post("/add")
async def create_timeline_post(
    new_timeline_object: TimelineInputDTO,
    timeline_dao: TimelinePostsDAO = Depends(),
) -> None:
    
    await timeline_dao.create_timeline_posts(
        user_id = new_timeline_object.user_id,
        content = new_timeline_object.content,
        image_url = new_timeline_object.image_url,
        hashtags = new_timeline_object.hashtags
    )
    
@router.get("/search", response_model=List[TimelinePostsDTO])
async def get_timeline_search_hashtag(
    hashtag: str,
    timeline_dao: TimelinePostsDAO = Depends()
) -> List[TimelinePostsModel]:
    
    return await timeline_dao.get_timeline_search_hashtag(hashtag=hashtag)