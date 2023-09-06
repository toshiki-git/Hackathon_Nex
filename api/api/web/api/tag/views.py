from typing import List

from fastapi import APIRouter,HTTPException
from fastapi.param_functions import Depends

from api.db.dao.game_tag import GameTagDAO
from api.db.models.game_tag_model import GameTagModel
from api.web.api.tag.schema import GameTagDTO

router = APIRouter()

@router.post("/create_tag")
async def create_game_tag(
    title: str,
    game_tag_dao: GameTagDAO = Depends(),
) -> None:

    return await game_tag_dao.create_game_tag(title=title)
    

@router.get("/get_tags", response_model=List[GameTagDTO])
async def get_game_tags(
    limit: int = 10,
    offset: int = 0,
    game_tag_dao: GameTagDAO = Depends(),
) -> List[GameTagModel]:

    game_tags = await game_tag_dao.get_game_tags(limit=limit, offset=offset)
    return game_tags

@router.get("/id_get", response_model=GameTagDTO)
async def get_tag_by_id(
    tag_id: int,
    game_tag_dao: GameTagDAO = Depends(),
) -> GameTagModel:

    game_tag = await game_tag_dao.get_game_tag_by_id(tag_id=tag_id)
    if game_tag is None:
        raise HTTPException(status_code=401, detail="Game tag not found")
    return game_tag



@router.get("/title_get", response_model=List[GameTagDTO])
async def get_tag_by_title(
    title: List[str],
    game_tag_dao: GameTagDAO = Depends(),
) -> List[GameTagModel]:

    game_tags = await game_tag_dao.get_game_tags_by_titles(titles=title)
    return game_tags