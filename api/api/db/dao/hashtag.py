from typing import List,Optional

from fastapi import Depends

from api.db.dependencies import get_db_session
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from api.db.models.hashtag_model import HashTagModel

class HashTagDAO:
    def __init__(self, session: AsyncSession = Depends(get_db_session)):
        self.session = session

    async def create_hashtag(self, hashtag: str) -> None:
        new_hash_tag = HashTagModel(hashtag=hashtag)
        self.session.add(new_hash_tag)

    async def get_hashtags(self, limit: int, offset: int) -> List[HashTagModel]:
        
        raw_timeline = await self.session.execute(
            select(HashTagModel).limit(limit).offset(offset),
        )

        return list(raw_timeline.scalars().fetchall())

    async def get_hashtag_by_id(self, tag_id: int) -> Optional[HashTagModel]:
        query = select(HashTagModel).filter(HashTagModel.id == tag_id)
        result = await self.session.execute(query)
        return result.scalars().first()
    
    async def get_hashtags_partial_by_title(self, hashtag: str) -> List[HashTagModel]:
        query = select(HashTagModel).filter(HashTagModel.hashtag.ilike(f'%{hashtag}%'))
        result = await self.session.execute(query)
        return list(result.scalars().fetchall())

    async def get_hashtags_exact_by_titles(self, hashtags: List[str]) -> List[HashTagModel]:
        query = select(HashTagModel).filter(HashTagModel.hashtag.in_(hashtags))
        result = await self.session.execute(query)
        return list(result.scalars().fetchall())
    
    async def get_hashtags_partial_bytitles(self, titles: List[str]) -> List[HashTagModel]:
        query = select(HashTagModel).filter(HashTagModel.title.ilike('%' + titles[0] + '%'))
        for title in titles[1:]:
            query = query.or_(HashTagModel.title.ilike('%' + title + '%'))

        result = await self.session.execute(query)
        return list(result.scalars().fetchall())