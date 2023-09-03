from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String

from api.db.base import Base

class TimelinePostsModel(Base):
    """Model for the timeline_posts table."""

    __tablename__ = "timeline_posts_model"

    post_id : Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id : Mapped[int] = mapped_column(Integer,nullable=False)
    content : Mapped[str] = mapped_column(String(length=500), nullable=False)
    image_url : Mapped[str] = mapped_column(String(length=200), nullable=True)

