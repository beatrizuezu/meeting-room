from unittest import mock

import pytest
from model_mommy import mommy
from rest_framework import status
from rest_framework.test import APIClient
from luizalabs_school.meetings.models import Room


URL = 'http://127.0.0.1:8000/v1/rooms/'


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def room():
    return mommy.make(
        Room,
        id=1,
        name='room_1',
        is_available=False
    )


@pytest.mark.django_db
class TestGetRooms(object):
    def test_should_get_all_rooms(self, client, room):
        response = client.get(URL)
        assert response.status_code == status.HTTP_200_OK
        assert len(response.json()) == 1

    def test_should_retrieve_specific_rooom_with_success(
        self,
        client,
        room
    ):
        response = client.get('{}{}/'.format(URL, 1))
        assert response.status_code == status.HTTP_200_OK
        assert response.json()['name'] == 'room_1'

    def test_should_retrieve_specific_rooom_without_success(
        self,
        client,
        room
    ):
        response = client.get('{}{}/'.format(URL, 4000))
        assert response.status_code == status.HTTP_404_NOT_FOUND


@pytest.mark.django_db
class TestPostRooms(object):
    def test_should_create_room_with_success(self, client):
        data = {
            'name': 'room_1',
            'is_available': True
        }
        response = client.post(URL, data=data)
        assert response.status_code == status.HTTP_201_CREATED

    def test_should_not_create_room_with_invalid_parameters(self, client):
        data = {
            'lalala': 'room_1',
            'active': True
        }
        response = client.post(URL, data=data)
        assert response.status_code == status.HTTP_400_BAD_REQUEST


@pytest.mark.django_db
class TestDeleteRooms(object):

    def test_should_delete_room(self, client, room):
        quantity_room = Room.objects.all().count()
        assert quantity_room == 1

        response = client.delete('{}{}/'.format(URL, 1))
        assert response.status_code == status.HTTP_204_NO_CONTENT

        quantity_room = Room.objects.all().count()
        assert quantity_room == 0


@pytest.mark.django_db
class TestPutRooms(object):

    def test_should_update_room_availability(self, client, room):
        data = {
            'name': 'room_1',
            'is_available': True
        }

        response = client.put('{}{}/'.format(URL, 1), data=data)
        assert response.status_code == status.HTTP_200_OK

        room = Room.objects.get(id=1)
        assert data['is_available'] == room.is_available


@pytest.mark.django_db
class TestPatchRomm(object):

    def test_should_update_room_availability_using_patch(self, client, room):
        data = {
            'is_available': True
        }
        response = client.patch('{}{}/'.format(URL, 1), data=data)
