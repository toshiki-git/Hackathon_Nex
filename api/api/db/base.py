from datetime import datetime

from sqlalchemy import DateTime
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from api.db.meta import meta
from api.static import static


class Base(DeclarativeBase):
    """Base for all models."""

    metadata = meta

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=datetime.now(static.TIME_ZONE),
        nullable=False,
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=datetime.now(static.TIME_ZONE),
        onupdate=datetime.now(static.TIME_ZONE),
        nullable=False,
    )
