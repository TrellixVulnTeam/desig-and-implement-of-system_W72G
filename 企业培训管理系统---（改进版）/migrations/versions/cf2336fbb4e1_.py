"""empty message

Revision ID: cf2336fbb4e1
Revises: eed949021102
Create Date: 2018-05-05 11:12:16.208485

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cf2336fbb4e1'
down_revision = 'eed949021102'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('courses', sa.Column('time', sa.String(length=32), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('courses', 'time')
    # ### end Alembic commands ###
