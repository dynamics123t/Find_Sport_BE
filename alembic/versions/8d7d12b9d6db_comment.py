"""comment

Revision ID: 8d7d12b9d6db
Revises: 919bdfa4f77d
Create Date: 2023-10-30 16:34:04.725411

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8d7d12b9d6db'
down_revision = '919bdfa4f77d'
branch_labels = None
depends_on = None

def upgrade():
    """
    Creates the comment table
    """
    op.create_table(
        'comment',
        sa.Column('id', sa.String(length=255), primary_key=True, nullable=False),
        sa.Column('id_user', sa.String(length=255), sa.ForeignKey('user.id', onupdate='CASCADE',
                  ondelete='CASCADE', deferrable=True)),
        # sa.Column('id_spost', sa.String(length=255), sa.ForeignKey('spost.id', onupdate='CASCADE',
        #           ondelete='CASCADE', deferrable=True)),
        sa.Column('content', sa.String(length=500), nullable=False),
        sa.Column('image', sa.String(length=256), nullable=True),
        sa.Column('time_create', sa.DateTime(), nullable=False, server_default=sa.text("(now() at time zone 'UTC')")),
    )


def downgrade():
    """
    Drops the comment table
    """
    op.drop_table('comment')