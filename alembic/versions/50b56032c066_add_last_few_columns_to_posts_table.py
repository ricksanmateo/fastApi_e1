"""add last few columns to posts table

Revision ID: 50b56032c066
Revises: 6bb865bee83a
Create Date: 2022-09-08 19:15:15.288243

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '50b56032c066'
down_revision = '6bb865bee83a'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column(
        'published', sa.Boolean(), nullable=False, server_default='TRUE'),)
    op.add_column('posts', sa.Column(
        'created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('NOW()')),)
    pass


def downgrade() -> None:
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass
