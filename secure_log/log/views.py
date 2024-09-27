from .models import Event
from django.shortcuts import render
from rest_framework import serializers, viewsets
from .dam import anon_bio, anon_username, anon_password, anon_name, anon_prompt, anon_response
from Crypto.Cipher import AES
from django.conf import settings

import os
import base64

def e(pt, k) -> bytes:
    c = AES.new(k, AES.MODE_GCM)
    ct, t = c.encrypt_and_digest(pt.encode('UTF-8'))
    return c.nonce + t + ct

def d(msg, k) -> str:
    ct = msg[32:]
    iv = msg[0:16]
    t = msg[16:32]

    c = AES.new(k, AES.MODE_GCM, iv)
    pt = c.decrypt_and_verify(ct, t)
    return pt.decode('UTF-8')

class EventSerializer(serializers.Serializer):
    event = serializers.CharField()
    time = serializers.DateTimeField()
    username = serializers.CharField()
    password = serializers.CharField()
    name = serializers.CharField()
    bio = serializers.CharField()
    prompt = serializers.CharField()
    response = serializers.CharField()
    
    def create(self, validated_data):
        k = settings.SECRET_KEY[:32].encode('utf-8')
        event = Event(
            event=validated_data['event'],
            time=validated_data['time'],
            username=e(anon_username(validated_data['username']), k),
            password=e(anon_password(validated_data['password']), k),
            name=e(anon_name(validated_data['name']), k),
            bio=e(anon_bio(validated_data['bio']), k),
            prompt=e(anon_prompt(validated_data['prompt']), k),
            response=e(anon_response(validated_data['response']), k)
        )
        event.save()
        return event
    def to_representation(self, instance):
        k = settings.SECRET_KEY[:32].encode('utf-8')
        rep = super().to_representation(instance)

        rep['event'] = instance.event
        rep['time'] = instance.time
        rep['username'] = d(instance.username, k)
        rep['password'] = d(instance.password, k)
        rep['name'] = d(instance.name, k)
        rep['bio'] = d(instance.bio, k)
        rep['prompt'] = d(instance.prompt, k)
        rep['response'] = d(instance.response, k)
        return rep
    

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer