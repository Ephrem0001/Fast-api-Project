"""create posts table

Revision ID: 1540c304ab3b
Revises: 
Create Date: 2025-08-30 19:14:12.217022

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1540c304ab3b'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table('posts',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('title', sa.String(length=100), nullable=False),
        sa.Column('content', sa.String(length=100), nullable=False)
        )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table('posts')
