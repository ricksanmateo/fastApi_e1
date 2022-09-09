"""add column to posts table

Revision ID: 063e6c5934f4
Revises: 525dd16b7685
Create Date: 2022-09-08 18:52:13.344814

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '063e6c5934f4'
down_revision = '525dd16b7685'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
