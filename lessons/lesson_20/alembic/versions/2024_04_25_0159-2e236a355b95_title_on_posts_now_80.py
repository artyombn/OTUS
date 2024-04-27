"""title on posts now 80

Revision ID: 2e236a355b95
Revises: e59d20cf08db
Create Date: 2024-04-25 01:59:49.319931

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = "2e236a355b95"
down_revision: Union[str, None] = "e59d20cf08db"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

table_name = "posts"


def upgrade() -> None:

    # Использование SQL кода в миграции
    # op.execute(
    #     """
    #     UPDATE posts
    #     SET title = substring(title, 0, 81)
    #     WHERE lenght(title) > 80
    # """
    # )

    metadata = sa.MetaData()
    metadata.reflect(
        bind=op.get_bind()
    )  # отображение структуры БД. сканирует БД и создает объекты SQLAlchemy

    table_posts = metadata.tables[table_name]
    stmt = (
        sa.update(table_posts)
        .where(sa.func.length(table_posts.c.title) > 80)
        .values({table_posts.c.title: sa.func.substring(table_posts.c.title, 0, 81)})
    )
    op.execute(stmt)

    op.alter_column(
        table_name,
        "title",
        existing_type=sa.VARCHAR(length=100),
        type_=sa.String(length=80),
        existing_nullable=False,
        existing_server_default=sa.text("''::character varying"),
    )


def downgrade() -> None:
    op.alter_column(
        table_name,
        "title",
        existing_type=sa.String(length=80),
        type_=sa.VARCHAR(length=100),
        existing_nullable=False,
        existing_server_default=sa.text("''::character varying"),
    )
