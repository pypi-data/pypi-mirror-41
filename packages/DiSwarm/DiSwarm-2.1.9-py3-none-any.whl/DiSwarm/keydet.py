from base64 import urlsafe_b64encode as enc
from datetime import date

def detkey(tok, cid):
    itok = [i for i in tok if i in '0123456789']
    key = str(int(int(('').join(itok)) * int(cid) / date.today().day)) + '15E97D8212D18D42F6EE12C954E14710C5C8A68BF2C20A3BA9D6FB7B4B8B0C45'
    key = enc(bytes(key + '=' * (len(key) % 4), 'utf-8'))
    return key
