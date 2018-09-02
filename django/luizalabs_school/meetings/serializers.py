from rest_framework import serializers

from luizalabs_school.meetings.models import Room


class RoomSerializer(serializers.ModelSerializer):
    name = serializers.CharField()
    is_available = serializers.BooleanField()

    class Meta:
        model = Room
        fields = ('name', 'is_available')
