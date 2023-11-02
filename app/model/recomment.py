from datetime import datetime

from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import relationship

from app.model.base import Base
from app.model.user import User


class Recomment(Base):
    __tablename__ = "recomment"

    id = Column(String(255), primary_key=True, index=True)
    id_user = Column(String(255), ForeignKey("user.id", ondelete="CASCADE", onupdate='CASCADE', deferrable=True))
    id_cmt = Column(String(255), ForeignKey("comment.id", ondelete="CASCADE", onupdate='CASCADE', deferrable=True))
    content = Column(String(1000))
    image = Column(String(255))
    time_create = Column(DateTime, default=datetime.now)

    # Relationship
    # user = relationship(User, back_populates="recomment")
    # comment = relationship("Comment", back_populates="recomment")
