import sqlalchemy
from sqlalchemy import orm

from app.core.database import mixins
from app.core.database.core import Base


class Template(Base, mixins.PrimaryKeyMixin, mixins.TimestampMixin):

    name: orm.Mapped[str] = orm.mapped_column(sqlalchemy.String(length=150), nullable=False)
