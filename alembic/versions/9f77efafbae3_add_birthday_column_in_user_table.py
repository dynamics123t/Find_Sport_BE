"""add birthday column in user table

Revision ID: 9f77efafbae3
Revises: c88831c322e7
Create Date: 2023-11-10 16:46:43.146801

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9f77efafbae3'
down_revision = 'c88831c322e7'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("user",sa.Column('birthday', sa.String(length=255), nullable=True)
                    )


def downgrade() -> None:
    op.drop_column("user", "birthday")