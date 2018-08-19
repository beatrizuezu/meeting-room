from rest_framework import serializers

from core.meetings.models import Room


class RoomSerializer(serializers.ModelSerializer):
    name = serializers.CharField()
    is_available = serializers.BooleanField()

    class Meta:
        model = Room
        fields = ('name', 'is_available')
