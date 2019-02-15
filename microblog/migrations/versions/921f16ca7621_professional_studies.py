"""professional_studies

Revision ID: 921f16ca7621
Revises: acc0a651f373
Create Date: 2019-02-15 12:34:45.491104

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '921f16ca7621'
down_revision = 'acc0a651f373'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('professional_studies',
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('start_date', sa.DATE(), nullable=True),
    sa.Column('end_date', sa.DATE(), nullable=True),
    sa.Column('society_name', sa.String(length=40), nullable=True),
    sa.Column('member_type', sa.String(length=40), nullable=True),
    sa.Column('status', sa.String(length=10), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('professional_studies')
    # ### end Alembic commands ###
