import os
import base64
from Crypto.Cipher import AES

def e(pt, k) -> bytes:
    c = AES.new(k, AES.MODE_GCM)
    ct, t = c.encrypt_and_digest(pt.encode('UTF-8'))
    return c.nonce + t + ct

def d(msg, k) -> str:
    if msg == None:
        return None

    ct = msg[32:]
    iv = msg[0:16]
    t = msg[16:32]

    c = AES.new(k, AES.MODE_GCM, iv)
    pt = c.decrypt_and_verify(ct, t)
    return pt.decode('UTF-8')