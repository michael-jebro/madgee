from flask import g
from .dict_structs import cloud_apps

from .db_schemas import (
    User, null
)


class AppNotFound(Exception):
    pass


APP_NOT_FOUND_ERR_MESS = 'requested application does not exist'


class CloudAppMaster:
    def __init__(self, user_id):
        self.user_id = user_id

    def get_all_apps(self):
        return cloud_apps

    def add_app(self, app_id):
        pass

    def get_app(self, app_id):
        user = g.db_session.query(User).filter(
            User.user_id == self.user_id,
            User.cloudapps[app_id] != null()
        ).first()

        if not user:
            raise AppNotFound(APP_NOT_FOUND_ERR_MESS)

        return user.cloudapps[app_id]

    def get_user_apps(self):
        user = g.db_session.query(User).filter(
            User.user_id == self.user_id
        ).first()

        return user.cloudapps
