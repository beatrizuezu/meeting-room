from rest_framework.viewsets import ModelViewSet
from core.api.meetings.serializers import RoomSerializer
from core.meetings.models import Room


class RoomViewSet(ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
