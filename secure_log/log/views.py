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
    template_name = 'events/event_list.html'

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        print(context)
        #context[""] = 
        return context
    