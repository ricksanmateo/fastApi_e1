"""add phone-number

Revision ID: 23ff793d44f4
Revises: 98b62bf5b746
Create Date: 2022-09-08 19:26:26.920483

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '23ff793d44f4'
down_revision = '98b62bf5b746'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('phone_number', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'phone_number')
    # ### end Alembic commands ###