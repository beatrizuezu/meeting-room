from django.db.models import Q
from rest_framework import serializers

from luizalabs_school.meetings.models import Meeting, Room


class RoomSerializer(serializers.ModelSerializer):

    class Meta:
        model = Room
        fields = '__all__'


class MeetingSerializer(serializers.ModelSerializer):
    room = serializers.PrimaryKeyRelatedField(
        queryset=Room.objects.all()
    )

    def validate(self, data):
        meeting = Meeting.objects.filter(
            Q(room=data['room']),
            Q(start_at__gte=data['start_at']) | Q(end_at__lte=data['start_at']),
            Q(start_at__gte=data['end_at']) | Q(end_at__lte=data['end_at'])
        )

        if meeting:
            raise serializers.ValidationError("room occupied")

        return data

    class Meta:
        model = Meeting
        fields = '__all__'
