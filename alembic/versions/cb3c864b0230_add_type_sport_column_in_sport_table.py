"""add type_sport column in sport table

Revision ID: cb3c864b0230
Revises: 5a5159abc744
Create Date: 2023-11-08 00:42:24.440089

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'cb3c864b0230'
down_revision = '5a5159abc744'
branch_labels = None
depends_on = None

sports_field_enum = sa.Enum("SOCCER", "TENNIS", "BASKETBALL", "BADMINTON", name='sports_field')

def upgrade() -> None:
    # Create the enum type
    sports_field_enum.create(op.get_bind())

    # Add the column using the enum type
    op.add_column(
        'sport',
        sa.Column(
            "sports_field",
            sports_field_enum,
            nullable=False,
            server_default="SOCCER"
        )
    )

def downgrade() -> None:
    op.drop_column("sport", "sports_field")
