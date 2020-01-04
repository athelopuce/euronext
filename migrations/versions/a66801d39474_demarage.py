"""demarage

Revision ID: a66801d39474
Revises: 
Create Date: 2020-01-03 09:48:24.913093

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a66801d39474'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('action',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.Column('symbole', sa.String(length=10), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_action_name'), 'action', ['name'], unique=True)
    op.create_index(op.f('ix_action_symbole'), 'action', ['symbole'], unique=True)
    op.create_table('ordre',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.Integer(), nullable=True),
    sa.Column('prix', sa.String(length=10), nullable=True),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.Column('action_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['action_id'], ['action.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('seuil',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('seuilMax', sa.Integer(), nullable=True),
    sa.Column('seuilMin', sa.Integer(), nullable=True),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.Column('action_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['action_id'], ['action.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('seuil')
    op.drop_table('ordre')
    op.drop_index(op.f('ix_action_symbole'), table_name='action')
    op.drop_index(op.f('ix_action_name'), table_name='action')
    op.drop_table('action')
    # ### end Alembic commands ###
