"""add foreign-key to posts table

Revision ID: 3e4bba280858
Revises: 3786ca10ce10
Create Date: 2025-08-31 22:57:39.050366

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3e4bba280858'
down_revision: Union[str, Sequence[str], None] = '3786ca10ce10'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
