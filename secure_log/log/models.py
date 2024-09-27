from django.db import models

class Event(models.Model):
    id = models.AutoField(primary_key=True)
    event = models.CharField(max_length=100)
    time = models.DateTimeField()
    username = models.BinaryField()
    password = models.BinaryField()
    name = models.BinaryField()
    bio = models.BinaryField()
    prompt = models.BinaryField()
    response = models.BinaryField()
    
