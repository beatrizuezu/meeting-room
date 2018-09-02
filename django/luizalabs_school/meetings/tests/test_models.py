import pytest
from model_mommy import mommy
from luizalabs_school.meetings.models import Room

@pytest.mark.django_db
class TestRoomModels(object):
    def test_shoul_assert_attributes(self):
        hasattr(Room, 'name')
        hasattr(Room, 'is_available')

    def test_should_assert_str(self):
        room = mommy.make(Room)

        assert str(room) == room.name
