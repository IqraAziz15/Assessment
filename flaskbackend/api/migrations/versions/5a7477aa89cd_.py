"""empty message

Revision ID: 5a7477aa89cd
Revises: e0619b178a0b
Create Date: 2021-01-03 20:51:52.287099

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5a7477aa89cd'
down_revision = 'e0619b178a0b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tableone',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('iso', sa.String(length=20), nullable=False),
    sa.Column('name', sa.String(length=20), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tableone')
    # ### end Alembic commands ###