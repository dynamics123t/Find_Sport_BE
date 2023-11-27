"""Add id_sport column to comment table

Revision ID: 46c8abaf0a61
Revises: 7a6027298b08
Create Date: 2023-11-27 13:21:59.114001

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '46c8abaf0a61'
down_revision = '7a6027298b08'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('comment', sa.Column('id_sport', sa.String(length=255), nullable=True))
    op.create_foreign_key('fk_comment_id_sport', 'comment', 'sport', ['id_sport'], ['id'], ondelete='CASCADE', onupdate='CASCADE')

def downgrade():
    op.drop_constraint('fk_comment_id_sport', 'comment', type_='foreignkey')
    op.drop_column('comment', 'id_sport')
