"""create tags table

Revision ID: 52c77754b548
Revises: 2e236a355b95
Create Date: 2024-04-26 20:26:58.190488

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = "52c77754b548"
down_revision: Union[str, None] = "2e236a355b95"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "tags",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(length=32), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("name"),
    )


def downgrade() -> None:
    op.drop_table("tags")
