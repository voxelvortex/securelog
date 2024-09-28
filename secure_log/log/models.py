from django.db import models

class Event(models.Model):
    id = models.AutoField(primary_key=True)
    event = models.CharField(max_length=100)
    time = models.DateTimeField(null=True)
    username = models.BinaryField(null=True)
    password = models.BinaryField(null=True)
    name = models.BinaryField(null=True)
    bio = models.BinaryField(null=True)
    prompt = models.BinaryField(null=True)
    response = models.BinaryField(null=True)
    
