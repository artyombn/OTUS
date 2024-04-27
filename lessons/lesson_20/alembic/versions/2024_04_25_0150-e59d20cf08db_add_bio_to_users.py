"""add bio to users

Revision ID: e59d20cf08db
Revises: 9f25ec6c3b22
Create Date: 2024-04-25 01:50:18.859318

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = "e59d20cf08db"
down_revision: Union[str, None] = "9f25ec6c3b22"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        "users",
        sa.Column(
            "bio",
            sa.String(length=200),
            nullable=True,
        ),
    )


def downgrade() -> None:
    op.drop_column(
        "users",
        "bio",
    )
