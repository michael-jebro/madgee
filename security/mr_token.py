from hashlib import sha256
from Crypto import Random
from .passwrod import Passwrod


class SessionId:
    def __init__(self, old_session=None):
        self.old_session = old_session

    def generate_session_idV1(self):
        random_str = Passwrod.RandomGenerator.get_random_string(100)
        hash = sha256(random_str.encode('utf-32')).hexdigest()
        return hash

    def generate_session_idV2(self):
        #TODO: play with jwt or use some lightweight cryptographic algorithm to sign the session cookie
        pass
