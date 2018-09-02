from rest_framework.viewsets import ModelViewSet
from luizalabs_school.meetings.serializers import RoomSerializer
from luizalabs_school.meetings.models import Room


class RoomViewSet(ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
