"""pagination step

Revision ID: 546842113621
Revises: 033c7ae2b589
Create Date: 2021-11-03 17:49:03.603360

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '546842113621'
down_revision = '033c7ae2b589'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('compositions', schema=None) as batch_op:
        batch_op.add_column(sa.Column('description_html', sa.Text(), nullable=True))
        batch_op.add_column(sa.Column('slug', sa.String(length=128), nullable=True))
        batch_op.create_unique_constraint('uq_composition_slug', ['slug'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('compositions', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')
        batch_op.drop_column('slug')
        batch_op.drop_column('description_html')

    # ### end Alembic commands ###