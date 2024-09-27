from models import *
from django.shortcuts import render
from rest_framework import serializers, viewsets

def _e(pt, k) -> bytes:
    c = AES.new(k, AES.MODE_GCM)
    ct, t = c.encrypt_and_digest(pt.encode('UTF-8'))
    return c.nonce + t + ct

def _d(msg, k) -> str:
    ct = msg[32:]
    iv = msg[0:16]
    t = msg[16:32]

    c = AES.new(k, AES.MODE_GCM, iv)
    pt = c.decrypt_and_verify(ct, t)
    return pt.decode('UTF-8')

class RegisterUserESerializer(serializers.ModelSerializer):
    class Meta:
        model = RegisterUserE
        exclude = ['id']
    
    def create(self, validated_data):
        register_user_e = RegisterUserE(
            time=validated_data['time'],
            username=
        )

class LoginUserESerializer(serializers.ModelSerializer):
    class Meta:
        model = LoginUserE
        exclude = ['id']

class MessageESerializer(serializers.ModelSerializer):
    class Meta:
        model = MessageE
        exclude = ['id']