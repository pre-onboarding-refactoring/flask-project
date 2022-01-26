"""empty message

Revision ID: 722c3abdcbfe
Revises: e5ab2e52c3dc
Create Date: 2022-01-26 22:56:50.234360

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '722c3abdcbfe'
down_revision = 'e5ab2e52c3dc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('lang', table_name='company_names')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index('lang', 'company_names', ['lang'], unique=False)
    # ### end Alembic commands ###
