from typing import List

from fastapi import APIRouter
from fastapi.param_functions import Depends

from api.db.models.timeline_posts_model import TimelinePostsModel
from api.db.dao.timeline_posts import TimelinePostsDAO
from api.web.api.timeline.public.schema import TimelinePostsDTO, TimelineInputDTO
from api.db.dao.game_tag import GameTagDAO

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
    game_tag_dao : GameTagDAO = Depends (),
    timeline_dao: TimelinePostsDAO = Depends(),
) -> None:
    
    game_tags = await game_tag_dao.get_tags_exact_by_titles(titles=new_timeline_object.game_titles)
    game_ids = [tag.id for tag in game_tags]
    
    #if not game_ids:
        #game_ids=[10]
    
    await timeline_dao.create_timeline_posts(
        user_id = new_timeline_object.user_id,
        content = new_timeline_object.content,
        image_url = new_timeline_object.image_url,
        game_ids = game_ids
    )
    
@router.get("/search", response_model=List[TimelinePostsDTO])
async def get_timeline_tag(
    game_id : int,
    timeline_dao: TimelinePostsDAO = Depends()
) -> List[TimelinePostsModel] :

    return await timeline_dao.get_timeline_tag(game_id=game_id)