from base64 import urlsafe_b64encode as enc
from datetime import date
import os

from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

def detkey(tok,chan):
    itok = ''.join([i for i in tok if i in '0123456789'])
    chbs = b'15E97D8212D18D42F6EE12C954E14710C5C8A68BF2C20A3BA9D6FB7B4B8B0C45'
    password = bytes(str(int(chan)*int(itok)),'utf-8') + chbs
    salt = bytes(str(itok),'utf-8')
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    key = enc(kdf.derive(password))
    return key

#detkey('12345adf','3274625748')
