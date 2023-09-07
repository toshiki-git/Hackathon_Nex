import secrets
from typing import List, Optional

from fastapi import Depends
from loguru import logger
from sqlalchemy import and_, select
from sqlalchemy.ext.asyncio import AsyncSession

from api.db.dependencies import get_db_session
from api.db.models.magic_link_model import MagicLinkModel

logger = logger.bind(task="Token")


class KeyTokenAlreadyExpiredError(Exception):
    """ "Error when tried to expire key_token was expired."""


class KeyTokenNotFoundError(Exception):
    """Error when not found key_token in database."""


class MagicLinkDAO:
    """Class for accessing token table."""

    def __init__(self, session: AsyncSession = Depends(get_db_session)):
        self.session = session

    def generate_seal(self, nbytes: Optional[int] = 48) -> str:
        """Fucntion to generate a key_token.

        :param nbytes:
            The string has *nbytes* random bytes.
            If *nbytes* is None or not supplied, a reasonable default is used.
        :returns: Returns the key_token
        """
        seal = secrets.token_urlsafe(nbytes)

        if self.is_seal_exist(seal=seal):
            seal = self.generate_seal()

        return seal

    async def create_magic_link(self, user_id: int) -> str:
        """Create key_token to create JWT token.

        :param user_id: The user_id is foreighn key of User table
        :returns: Returns generated key_token
        """
        token = self.generate_seal()
        self.session.add(
            MagicLinkModel(user_id=user_id, token=token),
        )

        return token

    async def get_magic_link(self, seal: str) -> List[MagicLinkModel]:
        """Function to get a same key_token for a given key.

        Just little little percent can able to generate same key,
        so this function returns a list

        :param key_token: The key_token string
        :returns:
            Returns same key_token was not used
            (!Expired key_token will also be RETURNS)
        """
        query = select(MagicLinkModel)
        query = query.filter(
            and_(MagicLinkModel.token == seal, MagicLinkModel.is_expired == False),
        )
        rows = await self.session.execute(query)

        return list(rows.scalars().fetchall())

    async def expire_magic_link(self, magik_link_id: int) -> None:
        """Function to expire a token.

        :param token_id: The id of the key_token at database
        :raises KeyTokenAlreadyExpiredError: If key_token is already key_token expired
        :raises KeyTokenNotFoundError: If not found key_token
        """
        token = await self.session.get(MagicLinkModel, magik_link_id)
        if token is not None:
            if not token.is_expired:
                logger.info(f"Expired token: (id: {token.id}) {token.token}")
                token.is_expired = True
            elif token.is_expired:
                logger.error("tried to expire token was expired.")
                raise KeyTokenAlreadyExpiredError()
        else:
            logger.error(f"Not found key_token: {token}")
            raise KeyTokenNotFoundError()

    async def is_seal_exist(self, seal: str) -> bool:
        query = select(MagicLinkModel)
        query = query.filter(MagicLinkModel.seal == seal)
        row = await self.session.execute(query)

        return row.one_or_none() is not None
