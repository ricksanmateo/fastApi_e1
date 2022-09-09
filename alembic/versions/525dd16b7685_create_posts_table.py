"""create posts table

Revision ID: 525dd16b7685
Revises: 
Create Date: 2022-09-08 17:37:27.226625

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '525dd16b7685'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('posts', sa.Column('id', sa.Integer(), nullable=False,
                    primary_key=True), sa.Column('title', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_table('posts')
    pass
