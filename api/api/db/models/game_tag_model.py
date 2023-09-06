from sqlalchemy import String
from sqlalchemy.orm import mapped_column, Mapped
from api.db.base import Base
    
class GameTagModel(Base):
    __tablename__ = "game_tag"

    id  : Mapped[int]  = mapped_column(primary_key=True, autoincrement=True)
    title : Mapped[str]  = mapped_column(String(length=100))