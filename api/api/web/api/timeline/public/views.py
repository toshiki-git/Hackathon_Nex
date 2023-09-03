from typing import List

from fastapi import APIRouter
from fastapi.param_functions import Depends

from api.db.models.timeline_posts_model import TimelinePostsModel
from api.db.dao.timeline_posts import TimelinePostsDAO
from api.web.api.timeline.public.schema import TimelinePostsSchema

router = APIRouter()

@router.get("/", response_model=List[TimelinePostsSchema])
async def timeline_post(
    limit: int = 10,
    offset: int = 0,
    timeline_dao: TimelinePostsDAO = Depends(),
    ) -> List[TimelinePostsModel] :
    
    return await timeline_dao.get_timeline_posts(limit=limit, offset=offset)

@router.put("/")
async def create_dummy_model(
    new_timeline_object: TimelinePostsSchema,
    timeline_dao: TimelinePostsDAO = Depends(),
) -> None:
    
    await timeline_dao.create_timeline_posts(
        user_id = new_timeline_object.user_id,
        content = new_timeline_object.content,
        image_url = new_timeline_object.image_url
    )