from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.types import Boolean, Integer, String

from api.db.base import Base
from api.db.models.user_model import UserModel


class TokenModel(Base):
    """Model for token."""

    __tablename__ = "token"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey(UserModel.id, onupdate="CASCADE", ondelete="CASCADE"),
    )
    token: Mapped[str] = mapped_column(String(100))
    is_expired: Mapped[bool] = mapped_column(Boolean, default=False)
