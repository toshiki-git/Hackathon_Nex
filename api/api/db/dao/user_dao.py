from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from api.db.dependencies import get_db_session


class UserDAO:
    """Class for accessing users table."""

    def __init__(self, session: AsyncSession = Depends(get_db_session)):
        self.session = session
