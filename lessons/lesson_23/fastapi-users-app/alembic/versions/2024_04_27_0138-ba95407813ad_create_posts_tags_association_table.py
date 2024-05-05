"""create posts tags association table

Revision ID: ba95407813ad
Revises: 52c77754b548
Create Date: 2024-04-27 01:38:17.402640

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = "ba95407813ad"
down_revision: Union[str, None] = "52c77754b548"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "posts_tags_association",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("post_id", sa.Integer(), nullable=False),
        sa.Column("tag_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["post_id"],
            ["posts.id"],
        ),
        sa.ForeignKeyConstraint(
            ["tag_id"],
            ["tags.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("post_id", "tag_id", name="unique_ix_post_tag"),
    )


def downgrade() -> None:
    op.drop_table("posts_tags_association")
