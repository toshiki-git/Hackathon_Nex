from typing import List, Optional

from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from api.db.dependencies import get_db_session
from api.db.models.timeline_posts_model import TimelinePostsModel


class TimelinePostsDAO:
    """Class for accessing timeline_posts table."""

    def __init__(self, session: AsyncSession = Depends(get_db_session)):
        self.session = session

    async def create_timeline_posts(
        self, user_id: int, content: str, image_url: Optional[str], hashtags: List[str]
    ) -> None:
        """Function to create timeline post.

        :param user_id: id of owner of post
        :param content: Content of post
        :param image_url: URL of image
        :param hashtags: List of hashtags
        """
        new_timeline_posts = TimelinePostsModel(
            user_id=user_id, content=content, image_url=image_url, hashtags=hashtags
        )

        self.session.add(new_timeline_posts)

    async def get_timeline_posts(
        self,
        limit: int,
        offset: int,
    ) -> List[TimelinePostsModel]:
        """Function to retrieve timeline posts.

        :param limit: Number of posts to retrieve
        :param offset: Offset of posts to retrieve
        :returns: List of model instances of post
        """
        raw_timeline = await self.session.execute(
            select(TimelinePostsModel).limit(limit).offset(offset),
        )

        return list(raw_timeline.scalars().fetchall())

    async def get_timeline_search_hashtag(
        self, hashtag: str
    ) -> List[TimelinePostsModel]:
        query = select(TimelinePostsModel)
        result = await self.session.execute(query)
        all_posts = result.scalars().fetchall()

        matching_posts = []

        for post in all_posts:
            if any(hashtag.lower() in tag.lower() for tag in post.hashtags):
                matching_posts.append(post)

        return matching_posts
