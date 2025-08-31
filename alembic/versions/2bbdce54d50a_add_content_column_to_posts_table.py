"""add content column to posts table

Revision ID: 2bbdce54d50a
Revises: 1540c304ab3b
Create Date: 2025-08-30 19:37:12.298288

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2bbdce54d50a'
down_revision: Union[str, Sequence[str], None] = '1540c304ab3b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False, server_default=''))    


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('posts', 'content')
