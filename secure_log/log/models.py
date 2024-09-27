from django.db import models

from encrypted_text import EncryptedTextField

class RegisterUserE(models.Model):
    id = models.AutoField(primary_key=True)
    time = models.DateTimeField()
    username = models.TextField()
    password = models.TextField()

class LoginUserE(models.Model):
    id = models.AutoField(primary_key=True)
    time = models.DateTimeField()
    username = models.TextField()
    password = models.TextField()

class MessageE(models.Model):
    id = models.AutoField(primary_key=True)
    time = models.DateTimeField()
    name = models.TextField()
    bio = models.TextField()
    prompt = models.TextField()
    response = models.TextField()
