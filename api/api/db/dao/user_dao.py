from ast import List
from typing import Optional

from fastapi import Depends
from loguru import logger
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from api.db.dependencies import get_db_session
from api.db.models.user_model import UserModel

logger = logger.bind(task="UserDAO")


class UserDAO:
    """Class for accessing users table."""

    def __init__(self, session: AsyncSession = Depends(get_db_session)):
        self.session = session

    async def get_user(self, user_id: int) -> Optional[UserModel]:
        """Function can get the user from user_id.

        If not found, return None

        :param user_id: id of the user you want to get.
        :returns: if not found user, will return None.
        """
        user = await self.session.get(UserModel, user_id)
        return user

    async def get_user_by_email(self, email: str) -> Optional[UserModel]:
        """Function can get the user from user_email.

        If not found, return None.

        :param email: email of the user you want to get.
        :returns: if not found user, will return None.
        """
        query = select(UserModel).where(UserModel.email == email)
        rows = await self.session.execute(query)

        return rows.scalar_one_or_none()

    async def create_user(self, username: str, email: str) -> int:
        """Function to create a new user.

        :param username: username of the user you want to create (max: 50 characters)
        :param email: email of the user you want to create (max: 255 characters)
        :raises ValueError: if the username or email maximum length is exceeded.
        :returns: if succeed to create user, will return user_id
        """
        if len(username) > 50:
            logger.error("Username maximum length exceeded.")
            raise ValueError("Username length cannot exceed 50 characters")
        if len(email) > 255:
            logger.error("Email maximum length exceeded.")
            raise ValueError("Username length cannot exceed 255 characters")

        user = UserModel(username=username, email=email)
        self.session.add(user)
        await self.session.commit()

        return user.id

    async def is_email_exists(self, email: str) -> bool:
        """Function to check if a user has already been created from an email.

        :param email: The email of user you want to check
        :returns:
            True if the email is already exists in the database.
            If not returns False.
        """
        query = select(UserModel).where(UserModel.email == email)
        rows = await self.session.execute(query)
        result = rows.scalar_one_or_none()

        return result is not None  
    