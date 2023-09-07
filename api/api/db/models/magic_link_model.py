from datetime import datetime, timedelta

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.types import Boolean, Integer, String

from api.db.base import Base
from api.static import static
from api.db.models.user_model import UserModel


class MagicLinkModel(Base):
    """Model for token."""

    __tablename__ = "token"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey(UserModel.id, onupdate="CASCADE", ondelete="CASCADE"),
    )
    seal: Mapped[str] = mapped_column(String(100))
    is_expired: Mapped[bool] = mapped_column(Boolean, default=False)

    def is_valid(self):
        if self.is_expired:
            return False

        expire_time = self.created_at + static.KEY_TOKEN_EXPIRE_TIME
        return datetime.now(static.TIME_ZONE) < expire_time
