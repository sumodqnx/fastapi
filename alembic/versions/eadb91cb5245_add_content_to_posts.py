"""add content to posts

Revision ID: eadb91cb5245
Revises: fc5c5952f556
Create Date: 2022-08-11 15:00:35.854486

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'eadb91cb5245'
down_revision = 'fc5c5952f556'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("posts", sa.Column("content", sa.String(), nullable=False))


def downgrade() -> None:
    op.drop_column("posts", "content")
