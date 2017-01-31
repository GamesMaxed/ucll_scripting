import hashlib
import base64
import os


def hash_password(password):
    # Create sha256
    sha = hashlib.sha256()

    # Feed it the password
    sha.update(password.encode('utf-8'))

    # Return the digest in hexadecimal form
    return sha.hexdigest()


def verify_password(password, hash):
    raise NotImplementedException()

def hash_salted_password(password):
    raise NotImplementedException()

def verify_salted_password(password, hash, salt):
    raise NotImplementedException()
