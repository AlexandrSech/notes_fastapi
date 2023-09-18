from datetime import datetime
import ormar
import sqlalchemy

from app.config import settings

from app.models.base import BaseMeta, metadata


class Board(ormar.Model):
    class Meta(BaseMeta):
        tablename = "boards"

    id: int = ormar.Integer(primary_key=True)
    name: str = ormar.String(max_length=255, unique=False, nullable=True)
    create_date: datetime = ormar.DateTime(timezone=True, nullable=True)
    update_date: datetime = ormar.DateTime(timezone=True, nullable=True)


engine = sqlalchemy.create_engine(settings.db_url)
metadata.create_all(engine)
