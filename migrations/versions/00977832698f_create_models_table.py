"""create models table

Revision ID: 00977832698f
Revises: 520aa6776347
Create Date: 2023-08-03 06:03:04.378071

"""
from alembic import op
import sqlalchemy as sa

revision = '00977832698f'
down_revision = '520aa6776347'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('models',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('model_name', sa.String(), nullable=False),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('end_point', sa.String(), nullable=False),
    sa.Column('model_provider_id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('models')
    # ### end Alembic commands ###