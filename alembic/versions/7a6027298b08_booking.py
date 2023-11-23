"""Booking

Revision ID: 7a6027298b08
Revises: 9f77efafbae3
Create Date: 2023-11-19 01:27:57.869231

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '7a6027298b08'
down_revision = '9f77efafbae3'
branch_labels = None
depends_on = None

mode_of_payment_enum = sa.Enum("CASH", "BANKING", name='mode_of_payment')
status_enum = sa.Enum("DA_DAT", "HUY", "DA_NHAN_SAN", "QUA_HAN", name='status_enum')


def upgrade() -> None:
    op.create_table('booking',
                    sa.Column('id', sa.String(length=255), nullable=False),
                    sa.Column('time_booking', sa.String(length=255), nullable=False),
                    sa.Column('date_booking', sa.Date(), server_default=sa.text('now()'), nullable=False),
                    sa.Column('time_create', sa.DateTime(), nullable=False,
                              server_default=sa.text("(now() at time zone 'UTC')")),
                    sa.Column(
                        "mode_of_payment",
                        mode_of_payment_enum,
                        nullable=False,
                        server_default="CASH"
                    ),
                    sa.Column(
                        "status",
                        status_enum,
                        nullable=False,
                        server_default="DA_NHAN_SAN"
                    ),

                    sa.Column('payment_status', sa.Boolean(), server_default=sa.text('false'), nullable=False),
                    sa.Column('id_user', sa.String(length=255), sa.ForeignKey('user.id', onupdate='CASCADE',
                                                                              ondelete='CASCADE', deferrable=True)),
                    sa.Column('id_sport', sa.String(length=255), sa.ForeignKey('sport.id', onupdate='CASCADE',
                                                                               ondelete='CASCADE', deferrable=True)),
                    sa.PrimaryKeyConstraint('id')
                    )


def downgrade() -> None:
    op.drop_table('booking')
