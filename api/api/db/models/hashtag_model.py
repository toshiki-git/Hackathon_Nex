from sqlalchemy import String
from sqlalchemy.orm import mapped_column, Mapped
from api.db.base import Base
    
class HashTagModel(Base):
    __tablename__ = "hash_tag"

    id  : Mapped[int]  = mapped_column(primary_key=True, autoincrement=True)
    hashtag : Mapped[str]  = mapped_column(String(length=100))