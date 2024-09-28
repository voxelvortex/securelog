from django.db import models
from .crypto import EncryptedField

class Event(models.Model):
    id = models.AutoField(primary_key=True)
    event = models.CharField(max_length=100)
    time = models.DateTimeField()
    username = EncryptedField(null=True)
    password = EncryptedField(null=True)
    name = EncryptedField(null=True)
    bio = EncryptedField(null=True)
    prompt = EncryptedField(null=True)
    response = EncryptedField(null=True)
    
