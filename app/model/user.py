from sqlalchemy import (Boolean, Column, Date, String, text, JSON, Integer, func, TIMESTAMP)
from sqlalchemy.orm import relationship

from app.model.base import Base, UserSystemRole


class User(Base):
    __tablename__ = "user"

    id = Column(String(255), primary_key=True)
    email = Column(String(255), nullable=False)
    username = Column(String(42), nullable=False)
    phone = Column(String(255), nullable=True)
    avatar = Column(String(255), nullable=True)
    address = Column(String(255), nullable=False)
    birthday = Column(String(255), nullable=True)
    is_active = Column(Boolean, nullable=False, server_default=text("false"))
    hashed_password = Column(String(255), nullable=True)
    verify_code = Column(String(255), nullable=True)
    system_role = Column(String(255), nullable=False, default=UserSystemRole.MEMBER)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text("now()"))
    updated_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text("now()"),
                        onupdate=func.current_timestamp())

