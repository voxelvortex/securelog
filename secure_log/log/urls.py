from django.urls import path, include
from .views import EventViewSet, EventListView
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'events', EventViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('events/', EventListView.as_view())
]
