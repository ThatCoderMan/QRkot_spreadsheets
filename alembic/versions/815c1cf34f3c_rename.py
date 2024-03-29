"""rename

Revision ID: 815c1cf34f3c
Revises: 6c466a855b17
Create Date: 2023-05-14 20:54:49.195877

"""
import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision = '815c1cf34f3c'
down_revision = '6c466a855b17'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('charityproject', schema=None) as batch_op:
        batch_op.add_column(sa.Column('create_date', sa.DateTime(), nullable=True))
        batch_op.drop_column('created_date')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('charityproject', schema=None) as batch_op:
        batch_op.add_column(sa.Column('created_date', sa.DATETIME(), nullable=True))
        batch_op.drop_column('create_date')

    # ### end Alembic commands ###
