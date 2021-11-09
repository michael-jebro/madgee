#TODO: put session into dbman so I could import it from here and use while being inside app contextim
from flask import g

from model.db_schemas import User
from sqlalchemy.orm.exc import NoResultFound

from security import (
    Passwrod, SessionId
)


# Exceptions
class LoginError(Exception):
    pass


class UsernameError(LoginError):
    pass


class NotPasswrodObject(LoginError):
    pass


class LoginFailed(LoginError):
    pass


#Error messages
USRNM_ERR_MESS = {
    'not_str': 'username param must be a string object'
}


NOT_PASSWD_OBJ_ERR_MESS = 'must be passwrod.Passwrod object'


LOGIN_FAIL_ERR_MESS = 'wrong login credentials'


class Login:
    def __init__(self, username, passwrod):
        self.__raise_errors_if_necessary(
            username, passwrod
        )

        self.username = username
        self.passwrod = passwrod

    def auth(self):
        user = g.db_session.query(User).filter(
            User.username == self.username
        ).first()

        if not user or not self.__passwords_match(user):
            raise LoginFailed(LOGIN_FAIL_ERR_MESS)

        session_id = SessionId().generate_session_idV1()
        return session_id

    def __passwords_match(self, user):
        return self.passwrod.the_same_as_(
            user.passwrod
        )

    def __raise_errors_if_necessary(self, username, passwrod):
        if not isinstance(username, str):
            raise UsernameError(USRNM_ERR_MESS['not_str'])

        if not isinstance(passwrod, Passwrod):
            raise NotPasswrodObject(NOT_PASSWD_OBJ_ERR_MESS)
