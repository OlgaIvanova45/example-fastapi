"""add content column to posts table

Revision ID: 69bb4c8cbe19
Revises: c91750007c3b
Create Date: 2022-08-16 07:42:22.066574

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '69bb4c8cbe19'
down_revision = 'c91750007c3b'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
