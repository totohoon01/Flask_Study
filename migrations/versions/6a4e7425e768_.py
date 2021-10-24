"""empty message

Revision ID: 6a4e7425e768
Revises: ee6d789c3ff8
Create Date: 2021-10-24 19:24:09.954907

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6a4e7425e768'
down_revision = 'ee6d789c3ff8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('answer', sa.Column('create_date', sa.DateTime(), nullable=False))
    op.drop_column('answer', 'create_data')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('answer', sa.Column('create_data', sa.DATETIME(), nullable=False))
    op.drop_column('answer', 'create_date')
    # ### end Alembic commands ###