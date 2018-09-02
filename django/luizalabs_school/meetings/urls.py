from rest_framework import routers
from django.conf.urls import include
from django.urls import path

from luizalabs_school.meetings.views import RoomViewSet


router = routers.DefaultRouter()
router.register(r'rooms', RoomViewSet)

urlpatterns = [
    path('', include(router.urls))
]
