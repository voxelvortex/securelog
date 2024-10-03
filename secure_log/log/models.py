from django.db import models
from .crypto import EncryptedField
import uuid

class UserUUID(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = EncryptedField(unique=True)

class UserData(models.Model):
    time = models.DateTimeField()
    user_uuid = models.ForeignKey('UserUUID', on_delete=models.CASCADE)
    password = EncryptedField(null=True)
    name = EncryptedField(null=True)
    bio = EncryptedField(null=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['time', 'user_uuid'], name='unique_time_useruuid'
            )
        ]

class Event(models.Model):
    id = models.AutoField(primary_key=True)
    event = models.CharField(max_length=100)
    time = models.DateTimeField()
    user_data = models.ForeignKey('UserData', on_delete=models.CASCADE)
    prompt = EncryptedField(null=True)
    response = EncryptedField(null=True)
    
