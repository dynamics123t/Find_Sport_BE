from datetime import datetime

from sqlalchemy import Column, Boolean, Date
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import relationship

from app.crud.base import Base
from app.model.base import StatusBookingEnum
from app.model.recomment import Recomment
from app.model.user import User


class Booking(Base):
    __tablename__ = "booking"

    id = Column(String(255), primary_key=True, index=True)
    id_user = Column(String(255), ForeignKey("user.id", ondelete="CASCADE", onupdate='CASCADE', deferrable=True))
    id_sport = Column(String(255), ForeignKey("sport.id", ondelete="CASCADE", onupdate='CASCADE', deferrable=True))
    time_create = Column(DateTime, default=datetime.now)
    time = Column(String(255), nullable=False)
    date = Column(Date(), nullable=False)
    mode_of_payment = Column(String(255))
    payment_status = Column(Boolean())
    status = Column(String(), default=StatusBookingEnum.DA_DAT)

