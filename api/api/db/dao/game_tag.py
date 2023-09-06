from typing import List,Optional

from fastapi import Depends

from api.db.dependencies import get_db_session
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from api.db.models.game_tag_model import GameTagModel

class GameTagDAO:
    def __init__(self, session: AsyncSession = Depends(get_db_session)):
        self.session = session

    async def create_game_tag(self, title: str) -> None:
        new_game_tag = GameTagModel(title=title)
        self.session.add(new_game_tag)

    async def get_game_tags(self, limit: int, offset: int) -> List[GameTagModel]:
        
        raw_timeline = await self.session.execute(
            select(GameTagModel).limit(limit).offset(offset),
        )

        return list(raw_timeline.scalars().fetchall())

    async def get_game_tag_by_id(self, tag_id: int) -> Optional[GameTagModel]:
        query = select(GameTagModel).filter(GameTagModel.id == tag_id)
        result = await self.session.execute(query)
        return result.scalars().first()
    
    async def get_game_tags_by_title(self, title: str) -> List[GameTagModel]:
        query = select(GameTagModel).filter(GameTagModel.title.ilike(f'%{title}%'))
        result = await self.session.execute(query)
        return list(result.scalars().all())
