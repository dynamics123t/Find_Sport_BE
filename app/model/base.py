from enum import Enum
from typing import Any

from sqlalchemy.ext.declarative import as_declarative, declared_attr


@as_declarative()
class Base:
    id: Any
    __name__: str

    # Generate __tablename__ automatically
    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()


class UserSystemRole(str, Enum):
    ADMIN = "ADMIN"
    MANAGER = "MANAGER"
    MEMBER = "MEMBER"


class CourseType(str, Enum):
    FREE = "FREE"
    PRO = "PRO"


class CourseRole(str, Enum):
    OWNER = "OWNER"
    MEMBER = "MEMBER"


class TypeSport(str, Enum):
    SOCCER = "SOCCER"
    TENNIS = "TENNIS"
    BASKETBALL = "BASKETBALL"
    BADMINTON = "BADMINTON"


class NotificationType(str, Enum):
    SYSTEM_NOTIFICATION = "SYSTEM_NOTIFICATION"
    COURSE_NOTIFICATION = "COURSE_NOTIFICATION"
    POST_NOTIFICATION = "POST_NOTIFICATION"
    COMMENT_NOTIFICATION = "COMMENT_NOTIFICATION"


class StatusBookingEnum(str, Enum):
    DA_DAT = "DA_DAT"
    HUY = "HUY"
    DA_NHAN_SAN = "DA_NHAN_SAN"
    QUA_HAN = "QUA_HAN"


class ModeOfPaymentEnum(str, Enum):
    CASH = "CASH"
    BANKING = "BANKING"


class TimeBookingEnum(str, Enum):
    TIME_5H = "5:00 - 6:00"
    TIME_6H = "6:00 - 7:00"
    TIME_7H = "7:00 - 8:00"
    TIME_8H = "8:00 - 9:00"
    TIME_9H = "9:00 - 10:00"
    TIME_10H = "10:00 - 11:00"
    TIME_11H = "11:00 - 12:00"
    TIME_12H = "12:00 - 13:00"
    TIME_13H = "13:00 - 14:00"
    TIME_14H = "14:00 - 15:00"
    TIME_15H = "15:00 - 16:00"
    TIME_16H = "16:00 - 17:00"
    TIME_17H = "17:00 - 18:00"
    TIME_18H = "18:00 - 19:00"
    TIME_19H = "19:00 - 20:00"
    TIME_20H = "20:00 - 21:00"
    TIME_21H = "21:00 - 22:00"
