from django.db import models

class EncryptedTextField(models.TextField):
    def __init__(self, *args, **kwargs):
        self.sk = *args['sk']
        super().__init__(*args, **kwargs)
    
    def to_python(self, value):
        if value is None:
            return value
        
        if isinstance(value, bytes):
            return self._d(value)
    
    def _e(self, pt) -> bytes:
        c = AES.new(self.sk, AES.MODE_GCM)
        ct, t = c.encrypt_and_digest(pt.encode('UTF-8'))
        return c.nonce + t + ct

    def _d(self, msg) -> str:
        ct = msg[32:]
        iv = msg[0:16]
        t = msg[16:32]

        c = AES.new(self.sk, AES.MODE_GCM, iv)
        pt = c.decrypt_and_verify(ct, t)
        return pt.decode('UTF-8')
