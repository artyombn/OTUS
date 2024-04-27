# Сложные связи в БД. alembic

**_SQLAlchemy many-to-many_**
_https://docs.sqlalchemy.org/en/20/orm/basic_relationships.html_

**_Пример новой таблицы, которая будет связывающим звеном_** 
```postgresql
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
```

_**Для создания связи добавляем `relationship()` в связывающие классы**_
```postgresql
    tags = relationship(
        # to tags (class name Tag)
        "Tag",
        # through this table
        secondary=posts_tags_association_table,
        # access this object through tag.posts
        back_populates="posts",
    )
```
_*Связываем posts с tags значит в tags пишем тоже самое_ 