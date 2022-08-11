"""create post table

Revision ID: fc5c5952f556
Revises: 
Create Date: 2022-08-11 14:40:24.709665

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fc5c5952f556'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table("posts", sa.Column("id", sa.Integer(), nullable=False, primary_key=True),
                            sa.Column("title", sa.String(), nullable=False))
    
def downgrade() -> None:
    op.drop_table("posts")
