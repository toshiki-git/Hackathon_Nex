from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql.sqltypes import String
from sqlalchemy_utils import EmailType

from api.db.base import Base


class UserModel(Base):
    """Model for user"""

    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(length=200))
    email: Mapped[EmailType] = mapped_column(EmailType, unique=True)
