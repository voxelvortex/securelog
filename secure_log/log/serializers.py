from django.shortcuts import render
from rest_framework import serializers, viewsets
from django.conf import settings

from .models import Event
from .dam import anon_bio, anon_username, anon_password, anon_name, anon_prompt, anon_response
from .crypto import e, d


class EventSerializer(serializers.Serializer):
    event = serializers.CharField()
    time = serializers.DateTimeField()
    username = serializers.CharField(required=False)
    password = serializers.CharField(required=False)
    name = serializers.CharField(required=False)
    bio = serializers.CharField(required=False)
    prompt = serializers.CharField(required=False)
    response = serializers.CharField(required=False)
    
    def create(self, validated_data):
        k = settings.SECRET_KEY[:32].encode('utf-8')
        event = Event(
            event=validated_data['event'],
            time=validated_data['time'],
            username=e(anon_username(validated_data['username']), k) if 'username' in validated_data else None,
            password=e(anon_password(validated_data['password']), k) if 'password' in validated_data else None,
            name=e(anon_name(validated_data['name']), k) if 'name' in validated_data else None,
            bio=e(anon_bio(validated_data['bio']), k) if 'bio' in validated_data else None,
            prompt=e(anon_prompt(validated_data['prompt']), k) if 'prompt' in validated_data else None,
            response=e(anon_response(validated_data['response']), k) if 'response' in validated_data else None
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