"""empty message

Revision ID: ee6d789c3ff8
Revises: 29d0a93c31a4
Create Date: 2021-10-24 11:24:24.826956

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ee6d789c3ff8'
down_revision = '29d0a93c31a4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('question', sa.Column('create_date', sa.DateTime(), nullable=False))
    op.drop_column('question', 'create_data')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('question', sa.Column('create_data', sa.DATETIME(), nullable=False))
    op.drop_column('question', 'create_date')
    # ### end Alembic commands ###
