"""empty message

Revision ID: 4fa04978120e
Revises: 
Create Date: 2021-01-29 17:17:12.074303

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '4fa04978120e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('email', sa.String(length=20), nullable=False))
    op.drop_index('username', table_name='user')
    op.create_unique_constraint(None, 'user', ['email'])
    op.drop_column('user', 'r_date')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('r_date', mysql.DATETIME(), nullable=True))
    op.drop_constraint(None, 'user', type_='unique')
    op.create_index('username', 'user', ['username'], unique=True)
    op.drop_column('user', 'email')
    # ### end Alembic commands ###
