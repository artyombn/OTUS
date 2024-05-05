"""create posts table

Revision ID: 9f25ec6c3b22
Revises: d24a95d4ca16
Create Date: 2024-04-25 01:41:54.298572

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = "9f25ec6c3b22"
down_revision: Union[str, None] = "d24a95d4ca16"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "posts",
        sa.Column(
            "id",
            sa.Integer(),
            nullable=False,
        ),
        sa.Column(
            "title",
            sa.String(length=100),
            server_default="",
            nullable=False,
        ),
        sa.Column(
            "body",
            sa.Text(),
            server_default="",
            nullable=True,
        ),
        sa.Column(
            "published_at",
            sa.DateTime(),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.Column(
            "user_id",
            sa.Integer(),
            nullable=False,
        ),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["users.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )


def downgrade() -> None:
    op.drop_table("posts")
