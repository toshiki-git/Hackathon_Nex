from datetime import datetime, timedelta

from sqlalchemy import ForeignKey
from sqlalchemy.ext.hybrid import hybrid_method
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.types import Boolean, Integer, String

from api.db.base import Base
from api.db.models.user_model import UserModel
from api.static import static


class MagicLinkModel(Base):
    """Model for token."""

    __tablename__ = "magic_link"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey(UserModel.id, onupdate="CASCADE", ondelete="CASCADE"),
    )
    seal: Mapped[str] = mapped_column(String(100))
    is_used: Mapped[bool] = mapped_column(Boolean, default=False)

    @hybrid_method
    def is_valid(self) -> bool:
        if self.is_used:
            return False

        expire_time = (
            self.created_at.astimezone(static.TIME_ZONE) + static.MAGIC_LINK_EXPIRE_TIME
        )
        return datetime.now(static.TIME_ZONE) < expire_time

    @hybrid_method
    def expire(self):
        self.is_used = True
