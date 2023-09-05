from sqlalchemy import ForeignKey, Column, Table

from sqlalchemy.orm import Mapped, mapped_column, relationship, DeclarativeBase
from sqlalchemy import Integer, String

from api.db.base import Base
from api.db.models.user_model import UserModel

from typing import List

class TimelinePostsModel(Base):
    """Model for the timeline_posts table."""

    __tablename__ = "timeline_posts"

    post_id : Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id : Mapped[int] = mapped_column(
        Integer,
        ForeignKey(UserModel.id, onupdate="CASCADE", ondelete="CASCADE"),
        nullable=False
    )
    content : Mapped[str] = mapped_column(String(length=500), nullable=False)
    image_url : Mapped[str] = mapped_column(String(length=200), nullable=True)
    
    game_tags = relationship("GameTag", secondary="timeline_post_tag_association")
    
    
class TimelineAssociationModel(DeclarativeBase):
    pass

timeline_post_tag_association = Table(
    "timeline_post_tag_association",
    Base.metadata,
    Column("timeline_post_id", Integer, ForeignKey("timeline_posts.post_id"), primary_key=True),
    Column("game_tag_id", Integer, ForeignKey("game_tag.id"), primary_key=True)
)


class GameTagModel(Base):
    """Model for the game_tags table."""

    __tablename__ = "game_tag"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String, index=True)

    timeline_posts: Mapped[List[TimelinePostsModel]] = relationship("TimelinePostsModel", secondary=timeline_post_tag_association, back_populates="game_tags")
