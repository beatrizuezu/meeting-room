from rest_framework import routers
from django.conf.urls import include
from django.urls import path

from luizalabs_school.meetings.views import MeetingViewSet, RoomViewSet


router = routers.DefaultRouter()
router.register(r'rooms', RoomViewSet)
router.register(r'meetings', MeetingViewSet)

urlpatterns = [
    path('', include(router.urls))
]
