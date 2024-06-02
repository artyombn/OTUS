"""create products table

Revision ID: 6d9505206602
Revises: 
Create Date: 2024-05-22 23:43:45.160960

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "6d9505206602"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "product",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(length=100), nullable=False),
        sa.Column("price", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("name"),
    )


def downgrade():
    op.drop_table("product")
