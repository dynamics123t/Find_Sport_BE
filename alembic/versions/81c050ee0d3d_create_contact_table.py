"""create contact table

Revision ID: 81c050ee0d3d
Revises: cb3c864b0230
Create Date: 2023-11-08 01:24:02.216831

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '81c050ee0d3d'
down_revision = 'cb3c864b0230'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table("contact", sa.Column("id", sa.String(length=255), nullable=False),
                    sa.Column("content", sa.String(length=1000), nullable=False),
                    sa.Column("user_id", sa.String(length=255), sa.ForeignKey('user.id', onupdate='CASCADE',
                                                                    ondelete='CASCADE', deferrable=True)),
                    sa.PrimaryKeyConstraint("id"))


def downgrade() -> None:
    op.drop_table('contact')
