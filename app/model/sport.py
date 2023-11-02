from sqlalchemy import (Boolean, Column, Date, String, text, JSON, Integer, func, TIMESTAMP, ForeignKey)
from sqlalchemy.orm import relationship

from app.model.base import Base


class Sport(Base):
    __tablename__ = "sport"

    id = Column(String(255), primary_key=True)
    name = Column(String(255), nullable=False)
    img = Column(String(255), nullable=False)
    description = Column(String(255), nullable=True)
    price = Column(String(255), nullable=False)
    address = Column(String(255), nullable=False)
    phone = Column(String(255), nullable=False)
    created_by = Column(String(), ForeignKey("user.id", ondelete="CASCADE", onupdate="CASCADE"))
    created_at = Column(TIMESTAMP(timezone=True), server_default=text("now()"))
    updated_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text("now()"),
                        onupdate=func.current_timestamp())
