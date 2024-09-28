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