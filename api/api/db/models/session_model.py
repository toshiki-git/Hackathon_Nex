from datetime import datetime, timedelta

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql.sqltypes import String, Integer, Boolean

from api.db.base import Base
from api.static import static
from api.db.models.user_model import UserModel


class SessionModel(Base):
    """Model for store session data."""

    __tablename__ = "dummy_model"

    id = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(
        Integer, ForeignKey(UserModel.id, onupdate="CASCADE", ondelete="CASCADE")
    )
    session_cert = mapped_column(String(128))
    refresh_token = mapped_column(String(128))
    is_expired: Mapped[bool] = mapped_column(Boolean, default=False)

    def is_valid(self):
        if self.is_expired:
            return False

        expire_time = self.created_at + static.REFRESH_TOKEN_EXPIRE_TIME
        return datetime.now(static.TIME_ZONE) < expire_time
