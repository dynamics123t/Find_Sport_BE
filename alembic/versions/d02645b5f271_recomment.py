"""recomment

Revision ID: d02645b5f271
Revises: 8d7d12b9d6db
Create Date: 2023-10-30 16:45:59.235907

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd02645b5f271'
down_revision = '8d7d12b9d6db'
branch_labels = None
depends_on = None


def upgrade():
    """
    Creates the recomment table
    """
    op.create_table(
        'recomment',
        sa.Column('id', sa.String(length=255), primary_key=True, nullable=False),
        sa.Column('id_user', sa.String(length=255), sa.ForeignKey('user.id', onupdate='CASCADE',
                                            ondelete='CASCADE', deferrable=True)),
        sa.Column('id_cmt', sa.String(length=255), sa.ForeignKey('comment.id', onupdate='CASCADE',
                                            ondelete='CASCADE', deferrable=True)),
        sa.Column('content', sa.String(length=500), nullable=False),
        sa.Column('image', sa.String(length=256), nullable=True),
        sa.Column('time_create', sa.DateTime(), nullable=False, server_default=sa.text("(now() at time zone 'UTC')")),
    )


def downgrade():
    """
    Drops the recomment table
    """
    op.drop_table('recomment')
