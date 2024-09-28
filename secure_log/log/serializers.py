from django.shortcuts import render
from rest_framework import serializers, viewsets

from .models import Event
from .dam import anon_bio, anon_username, anon_password, anon_name, anon_prompt, anon_response


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
        event = Event(
            event=validated_data['event'],
            time=validated_data['time'],
            username=anon_username(validated_data['username']) if 'username' in validated_data else None,
            password=anon_password(validated_data['password']) if 'password' in validated_data else None,
            name=anon_name(validated_data['name']) if 'name' in validated_data else None,
            bio=anon_bio(validated_data['bio']) if 'bio' in validated_data else None,
            prompt=anon_prompt(validated_data['prompt']) if 'prompt' in validated_data else None,
            response=anon_response(validated_data['response']) if 'response' in validated_data else None
        )
        event.save()
        return event