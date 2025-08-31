"""add foreign-key to posts table

Revision ID: 3786ca10ce10
Revises: dbaee72642f4
Create Date: 2025-08-30 20:28:24.701192

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3786ca10ce10'
down_revision: Union[str, Sequence[str], None] = 'dbaee72642f4'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('post_users_fk', source_table='posts', referent_table='users', local_cols=['owner_id'], remote_cols=['id'], ondelete='CASCADE')


def downgrade() -> None:
    """Downgrade schema."""
    pass
