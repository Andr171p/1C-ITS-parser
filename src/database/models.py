from sqlalchemy import Text
from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase

from pgvector.sqlalchemy import Vector


class BaseModel(AsyncAttrs, DeclarativeBase):
    __abstract__ = True

    id: Mapped[int] = mapped_column(
        autoincrement=True,
        primary_key=True
    )


class ProgramProductModel(BaseModel):
    __tablename__ = "program_products"

    url: Mapped[str]
    url_pattern: Mapped[str]
    name: Mapped[str]
    description: Mapped[str] = mapped_column(Text)
    embedding: Mapped[Vector] = mapped_column(Vector)
