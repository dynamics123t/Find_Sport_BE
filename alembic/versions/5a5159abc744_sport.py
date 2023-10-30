"""sport

Revision ID: 5a5159abc744
Revises: d02645b5f271
Create Date: 2023-10-30 17:13:19.352434

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5a5159abc744'
down_revision = 'd02645b5f271'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('sport',
                    sa.Column('id', sa.String(length=255), nullable=False),
                    sa.Column('name', sa.String(length=255), nullable=False),
                    sa.Column('img', sa.String(length=255), nullable=True),
                    sa.Column('description', sa.String(length=255), nullable=True),
                    sa.Column('price', sa.String(length=255), nullable=True),
                    sa.Column('address', sa.String(length=255), nullable=True),
                    sa.Column('phone', sa.String(length=255), nullable=True),
                    sa.Column('created_by', sa.String(length=255), nullable=False),
                    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
                    sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
                    sa.ForeignKeyConstraint(['created_by'], ['user.id'], ondelete="CASCADE"),
                    sa.PrimaryKeyConstraint('id')
                    )
def downgrade() -> None:
    op.drop_table('sport')