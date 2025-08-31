"""add content column to posts table

Revision ID: 20dc8cf6043b
Revises: f970dcfa432b
Create Date: 2025-08-30 19:40:03.478972

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '20dc8cf6043b'
down_revision: Union[str, Sequence[str], None] = 'f970dcfa432b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
