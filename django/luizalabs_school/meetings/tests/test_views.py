import mock
import pytest
import requests
from model_mommy import mommy

from rest_framework import status

from luizalabs_school.meetings.models import Room


def create_room(quantity, **kwargs):
    return mommy.make(
        Room,
        _quantity=quantity,
        **kwargs
    )


@pytest.mark.django_db
class TestGetRooms(object):
    url = 'http://127.0.0.1:8000/v1/rooms/'

    def test_should_get_all_rooms(self):
        pytest.set_trace()
        create_room(quantity=3)
        response = requests.get(self.url)

        assert response.status_code == status.HTTP_200_OK
        assert len(response.json()) == 3

    def test_should_retrieve_specific_rooom_with_success(self):
        kwargs = {
            'id': 1,
            'name': 'room_1',
            'is_available': True
        }
        room = create_room(quantity=1, **kwargs)
        pytest.set_trace()
        response = requests.get('{}{}'.format(self.url, 1))
        assert response.status_code == status.HTTP_200_OK
        assert response.json()['name'] == 'room_1'

    def test_should_retrieve_specific_rooom_without_success(self):
        kwargs = {
            'id': 1,
            'name': 'room_1',
            'is_available': True
        }
        create_room(quantity=1, **kwargs)
        response = requests.get('{}{}'.format(self.url, 4000))
        assert response.status_code == status.HTTP_404_NOT_FOUND
#
#
# @pytest.mark.django_db
# class TestPostRooms(object):
#     url = 'http://127.0.0.1:8000/v1/rooms/'
#
#     def test_should_create_room_with_success(self):
#         data = {
#             'name': 'room_1',
#             'is_available': True
#         }
#         response = requests.post(self.url, data=data)
#         assert response.status_code == status.HTTP_201_CREATED
#         assert response.headers['content-type'] == 'application/json'
#
#     def test_should_not_create_room_with_invalid_parameters(self):
#         data = {
#             'lalala': 'room_1',
#             'active': True
#         }
#         response = requests.post(self.url, data=data)
#         assert response.status_code == status.HTTP_400_BAD_REQUEST
#
#
# @pytest.mark.django_db
# class TestDeleteRomm(object):
#     url = 'http://127.0.0.1:8000/v1/rooms/'
#
#     def test_should_delete_room(self):
#         kwargs = {
#             'id': 1,
#             'name': 'room_1',
#             'is_available': False
#         }
#         room = create_room(quantity=1, **kwargs)
#         pytest.set_trace()
#         quantity_room = Room.objects.all().count()
#         assert quantity_room == 1
#
#         response = requests.delete('{}{}'.format(self.url, 1))
#         assert response.status_code == status.HTTP_204_NO_CONTENT
#
#         quantity_room = Room.objects.all().count()
#         assert quantity_room == 0
#

# @pytest.mark.django_db
# class TestPutRomm(object):
#     url = 'http://127.0.0.1:8000/v1/rooms/'
#
#     def test_should_update_room_availability(self):
#         kwargs = {
#             'id': 1,
#             'name': 'room_1',
#             'is_available': False
#         }
#         create_room(quantity=1, **kwargs)
#
#         data = {
#             'name': 'room_1',
#             'is_available': True
#         }
#         method_json = mock.MagicMock(return_value=data)
#
#         with mock.patch('requests.post') as put_mock:
#             put_mock.return_value = mock.MagicMock(
#             status_code=status.HTTP_200_OK,
#             json=method_json
#             )
#             response = requests.put('{}{}'.format(self.url, 1), data=data)


# @pytest.mark.django_db
# class TestPatchRomm(object):
#     url = 'http://127.0.0.1:8000/v1/rooms/'
#     def test_should_update_room_availability_using_patch(self):
#         kwargs = {
#             'id': 1,
#             'name': 'room_1',
#             'is_available': False
#         }
#         create_room(quantity=1, **kwargs)
#         data = {
#             'is_available': True
#         }
#         pytest.set_trace()
#         response = requests.patch('{}{}'.format(self.url, 1), data=data)
