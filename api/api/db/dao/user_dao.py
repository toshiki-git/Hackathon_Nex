from typing import Optional

from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from api.db.dependencies import get_db_session
from api.db.models.user_model import UserModel


class UserDAO:
    """Class for accessing users table."""

    def __init__(self, session: AsyncSession = Depends(get_db_session)):
        self.session = session

    async def get_user(self, id: int) -> Optional[UserModel]:
        query = select(UserModel).where(UserModel.id == id)
        rows = await self.session.execute(query)
        result = rows.scalar_one_or_none()
        return result

    async def get_user_by_email(self, email: str) -> Optional[UserModel]:
        query = select(UserModel).where(UserModel.email == email)
        rows = await self.session.execute(query)
        result = rows.scalar_one_or_none()
        return result

    async def create_user(self, username: str, email: str) -> int:
        if len(username) > 50:
            raise ValueError("Username length cannot exceed 50 characters")
        if len(email) > 255:
            raise ValueError("Username length cannot exceed 255 characters")

        user = UserModel(username=username, email=email)
        self.session.add(user)
        await self.session.commit()

        return user.id

    async def is_email_exists(self, email: str) -> bool:
        query = select(UserModel).where(UserModel.email == email)
        rows = await self.session.execute(query)
        result = rows.scalar_one_or_none()
        return result is not None
