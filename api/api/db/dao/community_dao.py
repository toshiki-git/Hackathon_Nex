from typing import List, Optional

from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from api.db.dependencies import get_db_session
from api.db.models.dummy_model import DummyModel
from api.db.models.community_model import CommunityModel


class CommunityDao:
    """Class for accessing dummy table."""

    def __init__(self, session: AsyncSession = Depends(get_db_session)):
        self.session = session
        
    async def create_community(self, user_id: int, community_id: int, content: str) -> None:
        self.session.add(CommunityModel(user_id=user_id, community_id=community_id, content=content))
        
    async def get_communities_by_community_id(self, community_id: int) -> List[CommunityModel]:
        stmt = select(CommunityModel).where(CommunityModel.community_id == community_id)
        result = await self.session.execute(stmt)
        communities = result.scalars().all()
        return communities