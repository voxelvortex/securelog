from django.shortcuts import render
from django.views.generic import ListView
from rest_framework import viewsets
import os
import base64
from django.conf import settings

from .serializers import EventSerializer
from .models import Event
from .crypto import d

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class EventListView(ListView):
    model = Event
    context_object_name = 'events'
    template_name = 'events/event_list.html'

    def get_queryset(self):
        queryset = Event.objects.all()
        key = settings.SECRET_KEY[:32].encode('utf-8')

        decrypted_events = []
        for event in queryset:
            decrypted_event = {
                'id': event.id,
                'event': event.event,
                'time': event.time,
                'username': d(event.username, key),
                'password': d(event.password, key),
                'name': d(event.name, key),
                'bio': d(event.bio, key),
                'prompt': d(event.prompt, key),
                'response': d(event.response, key)
            }
            decrypted_events.append(decrypted_event)

        return decrypted_events