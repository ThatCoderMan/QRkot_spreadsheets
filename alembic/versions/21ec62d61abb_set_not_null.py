"""init migration

Revision ID: 21ec62d61abb
Revises: c58004d27e9e
Create Date: 2023-05-14 20:34:17.262010

"""
import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision = '21ec62d61abb'
down_revision = 'c58004d27e9e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('charityproject', schema=None) as batch_op:
        batch_op.alter_column('description',
               existing_type=sa.TEXT(),
               nullable=False)
        batch_op.alter_column('full_amount',
               existing_type=sa.INTEGER(),
               nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('charityproject', schema=None) as batch_op:
        batch_op.alter_column('full_amount',
               existing_type=sa.INTEGER(),
               nullable=True)
        batch_op.alter_column('description',
               existing_type=sa.TEXT(),
               nullable=True)

    # ### end Alembic commands ###
