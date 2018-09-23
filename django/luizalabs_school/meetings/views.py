from rest_framework.viewsets import ModelViewSet
from luizalabs_school.meetings.serializers import (
    MeetingSerializer,
    RoomSerializer
)
from luizalabs_school.meetings.models import Meeting, Room


class RoomViewSet(ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class MeetingViewSet(ModelViewSet):
    queryset = Meeting.objects.all()
    serializer_class = MeetingSerializer
