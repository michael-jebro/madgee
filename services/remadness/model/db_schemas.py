from dbman import Base

from sqlalchemy import (
    Column, Integer, String, Text, CHAR
)


class Device(Base):
    __tablename__ = 'devices'

    device_id = Column(Text, unique=True, primary_key=True)
    user_id = Column(Integer, unique=True, primary_key=True)
    username = Column(String(30), unique=True, nullable=False)
    email = Column(String(50), unique=True, nullable=False)
    phone = Column(Integer, unique=False, nullable=True)
    password = Column(CHAR(64), unique=False, nullable=False)
    salt = Column(CHAR(50), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.user_id


class Permission():
    pass

class Stats():
    pass

class Log():
    pass