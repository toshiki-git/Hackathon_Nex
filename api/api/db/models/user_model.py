from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql.sqltypes import String, Boolean
from sqlalchemy_utils import EmailType

from api.db.base import Base


class UserModel(Base):
    """Model for user."""

    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column(String(length=50), nullable = True)
    display_name: Mapped[str] = mapped_column(String(length=50), nullable = False)
    is_initialized: Mapped[bool] = mapped_column(Boolean, default=False)
    email: Mapped[EmailType] = mapped_column(EmailType, unique=True)
