import hashlib
import base64


def hash_password(password):
    # Create sha256
    sha = hashlib.sha256()

    # Feed it the password
    sha.update(password.encode('utf-8'))

    # Return the digest in hexadecimal form
    return sha.hexdigest()


def verify_password(password, hash):
    return hash_password(password) == hash


def hash_salted_password(password, salt):
    sha = hashlib.sha256()

    sha.update(password.encode('utf-8'))
    sha.update(salt.encode('utf-8'))

    return sha.hexdigest()


def verify_salted_password(password, hash, salt):
    return hash_salted_password(password, salt) == hash



    
    
    
