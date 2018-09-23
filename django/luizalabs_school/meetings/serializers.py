from rest_framework import serializers

from luizalabs_school.meetings.models import Meeting, Room


class RoomSerializer(serializers.ModelSerializer):

    class Meta:
        model = Room
        fields = '__all__'


class MeetingSerializer(serializers.ModelSerializer):
    room = serializers.PrimaryKeyRelatedField(
        queryset=Room.objects.filter(is_available=True)
    )
    class Meta:
        model = Meeting
        fields = '__all__'
