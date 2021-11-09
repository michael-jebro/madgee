import string
import random
from hashlib import pbkdf2_hmac

__author__ = 'michael-jebro'
__version__ = '2.0'
__license__ = 'BSD 3-clause'


PASS_ERR_MESS = {
    'too_short': 'password must be at least 8 chars long',
    'not_str': 'password value must be a string'
}


SALT_ERR_MESS = {
    'too_short': 'salt is too short (at least 30 characters)',
    'not_str': 'salt value must be a string'
}

HASH_NOT_MATCH_MESS = 'hash does not match the target one'


class PasswrodError(Exception):
    pass


class PasswordError(PasswrodError):
    pass


class SaltError(PasswrodError):
    pass


class HashesDoNotMatch(PasswrodError):
    pass


class Passwrod:

    class RandomGenerator:
        @staticmethod
        def get_random_string(length):
            random_string = ''.join(
                [random.SystemRandom().choice(string.printable) for _ in range(0, length)]
            )

            return random_string


    def __init__(self, password, salt):
        self.__throw_errors_if_necessary(
            password,
            salt
        )

        self.__passwrod = password
        self.__salt = salt

    def the_same_as_(self, target_hash):
        self_hash = self.__gen_hash_of_(self.__passwrod)
        return self_hash == target_hash

    def compare(self, target_hash):
        self_hash = self.__gen_hash_of_(self.__passwrod)
        if not self_hash == target_hash:
            raise HashesDoNotMatch(HASH_NOT_MATCH_MESS)

    def get_hash(self):
        hashed_item = self.__gen_hash_of_(self.__passwrod)
        return hashed_item

    def get_salt(self):
        return self.__salt

    def __gen_hash_of_(self, password):
        alg = 'sha256'
        iters = 1500
        pbkdf2_hash = pbkdf2_hmac(
            alg,
            password.encode('utf-32'),
            self.__salt.encode('utf-32'),
            iters
        )

        return pbkdf2_hash.hex()

    def __throw_errors_if_necessary(self, password, salt):
        if not isinstance(password, str):
            raise PasswordError(PASS_ERR_MESS['not_str'])

        if not isinstance(salt, str):
            raise SaltError(SALT_ERR_MESS['not_str'])

        if not len(password) >= 8:
            raise PasswordError(PASS_ERR_MESS['too_short'])

        if not len(salt) >= 30:
            raise PasswordError(SALT_ERR_MESS['too_short'])
