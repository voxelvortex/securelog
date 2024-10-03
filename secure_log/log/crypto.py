import os
import base64
from Crypto.Cipher import AES
from django.db import models

from django.conf import settings

def k() -> bytes:
    return settings.SECRET_KEY[:32].encode('utf-8')

def e(pt, k) -> bytes:
    if pt is None:
        return None

    print(pt)
    c = AES.new(k, AES.MODE_GCM)
    ct, t = c.encrypt_and_digest(pt.encode('UTF-8'))
    return c.nonce + t + ct

def d(msg, k) -> str:
    if msg is None:
        return None

    ct = msg[32:]
    iv = msg[0:16]
    t = msg[16:32]

    c = AES.new(k, AES.MODE_GCM, iv)
    pt = c.decrypt_and_verify(ct, t)
    return pt.decode('UTF-8')

class EncryptedField(models.BinaryField):
    def get_prep_value(self, value):
        if value is None:
            return value
        else:
            return e(value, k())
    
    def from_db_value(self, value, expression, connection):
        if value is None:
            return None
        else:
            return d(value, k())

    def to_python(self, value):
        if value is None or isinstance(value, str):
            return value
        else:
            return d(value, k())
