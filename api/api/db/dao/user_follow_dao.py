
from typing import List, Optional

from fastapi import Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from api.db.dependencies import get_db_session
from api.db.models.user_follow_model import FollowModel


class FollowDAO:
    """Class for follow table."""

    def __init__(self, session: AsyncSession = Depends(get_db_session)):
        self.session = session
    
    async def get_user_followers(self, user_id: int) -> List[int]:
        # user_id に一致するすべての行を取得するクエリを作成
        query = select(FollowModel).where(FollowModel.user_id == user_id)
        
        # クエリを実行して結果を取得
        result = await self.session.execute(query)
        rows = result.scalars().all()
        
        # following_id を配列に追加する処理
        following_ids = [row.following_id for row in rows if row.following_id is not None]
        
        return following_ids
    
    async def create_follow(self, follower_id: int, following_id: int) -> FollowModel:
        # Create new follow relationship
        new_follow = FollowModel(follower_id=follower_id, following_id=following_id)
        self.session.add(new_follow)
        await self.session.commit()


    async def delete_follow(self, follower_id: int, following_id: int) -> None:
        # Delete the relationship
        self.session.delete(following_id)
        await self.session.commit()


