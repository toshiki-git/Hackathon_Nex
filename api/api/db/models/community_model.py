from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql.sqltypes import String, Integer
from api.db.models.user_model import UserModel
from api.db.models.timeline_posts_model import TimelinePostsModel
from sqlalchemy import ForeignKey
from api.db.base import Base


class CommunityModel(Base):

    __tablename__ = "community"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id : Mapped[int] = mapped_column(     
        Integer,
        ForeignKey(UserModel.id, onupdate="CASCADE", ondelete="CASCADE"),
        nullable=False,
        )
    community_id : Mapped[int] = mapped_column(
        Integer,
        ForeignKey(TimelinePostsModel.post_id, onupdate="CASCADE", ondelete="CASCADE"),
        nullable=False,
    )
    content : Mapped[str] = mapped_column(String(length=200))
