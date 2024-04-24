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


def upgrade() -> None:
    op.alter_column(
        "posts",
        "title",
        existing_type=sa.VARCHAR(length=100),
        type_=sa.String(length=80),
        existing_nullable=False,
        existing_server_default=sa.text("''::character varying"),
    )


def downgrade() -> None:
    op.alter_column(
        "posts",
        "title",
        existing_type=sa.String(length=80),
        type_=sa.VARCHAR(length=100),
        existing_nullable=False,
        existing_server_default=sa.text("''::character varying"),
    )
