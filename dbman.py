from os import path
from json import load
from flask import g as shared_
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base


'''
# Exceptions
class SessionShareError(Exception):
    pass


# Exception messages
SESS_SHARE_ERR_MESS = {
    'already_exists': 'database session object already exists in g',
    'doesnt_exist': 'database session object doesn\'t exist in g'
}
'''


class DBConfMan:
    def __init__(self, path_to_mgconf):
        mgconf = open(path_to_mgconf, 'r')
        conf_data = load(mgconf)
        self.data = conf_data['_DB']

    def get_uri(self):
        alias = self.data['_alias']

        return "{0}://{1}:{2}@{3}:{4}/{5}".format(
            alias['driver'], alias['username'], alias['passwrod'],
            alias['hostname'], alias['port'], alias['db_name']
        )


'''
#TODO
class DBSessionMan:
    __slots__ = ['__session']

    def __new__(cls, session=None):
        if session:
            cls.__session = session
        return super(DBSessionMan, cls).__new__(cls)

    @staticmethod
    def get_session():
        return shared_.db_session

    def share_session(self):
        if 'db_session' not in shared_:
            shared_.db_session = self.__session
        else:
            raise SessionShareError(SESS_SHARE_ERR_MESS['already_exists'])

    def refresh_session(self):
        if 'db_session' in shared_:
            shared_.db_session.remove()
            shared_.pop('db_session')
        else:
            raise SessionShareError(SESS_SHARE_ERR_MESS['doesnt_exist'])
'''


Base = declarative_base()
dbconfman = DBConfMan(path.abspath('mgconf.json'))
engine = create_engine(dbconfman.get_uri())


def create_all():
    Base.metadata.create_all(bind=engine)

