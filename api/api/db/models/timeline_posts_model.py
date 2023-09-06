from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import mapped_column, Mapped
from api.db.base import Base
from api.db.models.user_model import UserModel
from sqlalchemy.dialects import postgresql as pg

class TimelinePostsModel(Base):
    """Model for the timeline_posts table."""
    __tablename__ = "timeline_post"

    post_id  : Mapped[int]  = mapped_column(primary_key=True, autoincrement=True)
    user_id : Mapped[int]  = mapped_column(Integer, ForeignKey(UserModel.id, onupdate="CASCADE", ondelete="CASCADE"), nullable=False)
    content : Mapped[str]  = mapped_column(String(length=500), nullable=False)
    image_url : Mapped[str]  = mapped_column(String(length=200), nullable=True)
    hashtags : Mapped[str] = mapped_column(pg.ARRAY(String(length=100)), nullable=True)
