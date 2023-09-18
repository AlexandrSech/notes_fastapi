from datetime import datetime
import ormar
import sqlalchemy
from typing import Optional, List

from app.config import settings

from app.models.base import BaseMeta, metadata
from app.models.board import Board


class Note(ormar.Model):
    class Meta(BaseMeta):
        tablename = "notes"

    id: int = ormar.Integer(primary_key=True)
    text: str = ormar.String(max_length=255, unique=False, nullable=False)
    create_date: datetime = ormar.DateTime(timezone=True, nullable=True)
    update_date: datetime = ormar.DateTime(timezone=True, nullable=True)
    views: int = ormar.Integer(nullable=True)
    boards: Optional[List[Board]] = ormar.ManyToMany(Board, nullable=True)


engine = sqlalchemy.create_engine(settings.db_url)
metadata.create_all(engine)
