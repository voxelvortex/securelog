from django.shortcuts import render
from rest_framework import serializers, viewsets

from .models import Event, UserData, UserUUID
from .dam import anon_bio, anon_username, anon_password, anon_name, anon_prompt, anon_response

from rest_framework import serializers
from .dam import anon_username, anon_password, anon_name, anon_bio, anon_prompt, anon_response

username_uuid = {}

@staticmethod
def update_username_uuid():
    username_uuid = {}
    for user in UserUUID.objects.all():
        username_uuid[user.username] = user

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
        a_username = anon_username(validated_data['username'])
        print(username_uuid)
        if a_username not in username_uuid.keys():
            update_username_uuid()
            print('nf')
        if a_username not in username_uuid.keys():
            print('nf2')
            user_uuid = UserUUID(
                username = a_username
            )
            user_uuid.save()
        else:
            print('f')
            user_uuid = username_uuid[a_username]

        print(user_uuid)
        user_data = UserData(
            time=validated_data['time'],
            user_uuid=user_uuid,
            password=anon_password(validated_data['password']) if 'password' in validated_data else None,
            name=anon_name(validated_data['name']) if 'name' in validated_data else None,
            bio=anon_bio(validated_data['bio']) if 'bio' in validated_data else None,
        )
        user_data.save()

        event = Event(
            event=validated_data['event'],
            time=validated_data['time'],
            user_data=user_data,
            prompt=anon_prompt(validated_data['prompt']) if 'prompt' in validated_data else None,
            response=anon_response(validated_data['response']) if 'response' in validated_data else None
        )
        event.save()

        return event