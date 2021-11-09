from dbman import Base

from sqlalchemy.dialects.postgresql.json import JSON

from sqlalchemy import (
    Column, Integer, String, CHAR, null
)


class User(Base):
    __tablename__ = 'users'

    user_id = Column(Integer, unique=True, primary_key=True)
    username = Column(String(30), unique=True, nullable=False)
    email = Column(String(50), unique=True, nullable=False)
    phone = Column(Integer, unique=False, nullable=True)
    passwrod = Column(CHAR(64), unique=False, nullable=False)
    salt = Column(CHAR(50), unique=False, nullable=False)

    plan = Column(CHAR(1), unique=False, nullable=False)
    device_amount = Column(Integer, unique=False, nullable=False)
    cloudapps = Column(JSON, nullable=True)

    def __repr__(self):
        return '<User %r>' % self.user_id
