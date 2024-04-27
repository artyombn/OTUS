# class PostsTagsAssociation()
from sqlalchemy import (
    Table,
    Column,
    ForeignKey,
    Integer,
    UniqueConstraint,
)

from .base import Base

posts_tags_association_table = Table(
    "posts_tags_association",
    Base.metadata,
    # Column("post_id", nullable=False, primary_key=True),
    # Column("tag_id", nullable=False, primary_key=True),
    # Лучше без primary_key, чтобы избежать в дальнейшем проблем
    Column("id", Integer, primary_key=True),
    Column("post_id", ForeignKey("posts.id"), nullable=False),
    Column("tag_id", ForeignKey("tags.id"), nullable=False),
    UniqueConstraint("post_id", "tag_id", name="unique_ix_post_tag"),
)
# не можем сделать уникальный tag_id иначе мы его не сможем потом привязать
