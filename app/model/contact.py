from sqlalchemy import Column, TIMESTAMP, text
from sqlalchemy import ForeignKey
from sqlalchemy import String

from app.crud.base import Base


class Contact(Base):
    __tablename__ = "contact"

    id = Column(String(255), primary_key=True, index=True)
    content = Column(String(255), nullable=False)
    user_id = Column(String(255), ForeignKey('user.id', onupdate="CASCADE", ondelete="CASCADE"))
    created_at = Column(TIMESTAMP(timezone=True), server_default=text("now()"))
