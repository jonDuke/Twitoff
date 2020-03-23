"""empty message

Revision ID: 331b5d3e9fcf
Revises: 
Create Date: 2020-03-23 14:03:05.294960

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '331b5d3e9fcf'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('book',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=128), nullable=True),
    sa.Column('author_id', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('book')
    # ### end Alembic commands ###
