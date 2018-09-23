from rest_framework import serializers

from luizalabs_school.meetings.models import Room


class RoomSerializer(serializers.ModelSerializer):

    class Meta:
        model = Room
        fields = ('name', 'is_available')
