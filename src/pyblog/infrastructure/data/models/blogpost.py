from datetime import datetime
from uuid import UUID
from typing import Optional

from sqlalchemy.orm import Mapped, mapped_column

from pyblog.infrastructure.data.base import Base

class BlogPostDAO(Base):
    __tablename__ = "blog_posts"

    id: Mapped[UUID] = mapped_column(primary_key=True)
    title: Mapped[str]
    slug: Mapped[str]
    markdown: Mapped[str]

    created_on: Mapped[datetime]
    published_on: Mapped[Optional[datetime]]
    last_updated_on: Mapped[datetime]
