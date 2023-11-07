"""add created_at column in contact table

Revision ID: c88831c322e7
Revises: 81c050ee0d3d
Create Date: 2023-11-08 01:46:23.733018

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'c88831c322e7'
down_revision = '81c050ee0d3d'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('contact',
                  sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True))


def downgrade() -> None:
    op.drop_column("contact", "created_at")
