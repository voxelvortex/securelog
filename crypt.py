from Crypto.Cipher import AES

import os
import base64

class AESGCM:
    def __init__(self, sk):
        if sk:
            self.sk = sk
        else:
            self.sk = os.urandom(32)
    
    def e(self, pt) -> bytes:
        c = AES.new(self.sk, AES.MODE_GCM)
        ct, t = c.encrypt_and_digest(pt.encode('UTF-8'))
        return c.nonce + t + ct

    def d(self, msg) -> str:
        ct = msg[32:]
        iv = msg[0:16]
        t = msg[16:32]

        c = AES.new(self.sk, AES.MODE_GCM, iv)
        pt = c.decrypt_and_verify(ct, t)
        return pt.decode('UTF-8')

obj = AESGCM(sk=None)
print(obj.d(obj.e('Hi Im max')))
