import string
import uuid
from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Optional
from uuid import UUID


@dataclass
class BlogPost:
    id: UUID
    title: string
    slug: string
    markdown: string

    created_on: datetime
    last_updated_on: datetime

    published_on: Optional[datetime]
    def is_published(self):
        return self.published_on is not None
    def publish(self):
        self.published_on = datetime.now(timezone.utc)

    @staticmethod
    def new_empty_post():
        return BlogPost(
            id=uuid.uuid4(),
            title="Untitled",
            slug="",
            created_on=datetime.now(timezone.utc),
            last_updated_on=datetime.now(timezone.utc),
            published_on=None,
            markdown=""
        )
