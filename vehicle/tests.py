from rest_framework.test import APITestCase
from rest_framework import status

from vehicle.models import Car


class VehicleTestCase(APITestCase):

    def setUp(self) -> None:
        pass

    def test_create_car(self):
        """Тестирование создание машины"""
        data = {
            "title": "Test",
            "descriptions": "Test"
        }
        response = self.client.post(
            '/cars/',
            data=data
        )

        self.assertEqual(response.json(),
                         {'id': 1, 'milage': [], 'title': 'Test', 'descriptions': 'Test', 'owner': None})

        self.assertTrue(
            Car.objects.all().count() == 1,
        )

    def test_list_cars(self):
        """Тестирование списка машин"""

        Car.objects.create(
            title="list test",
            descriptions="list test",
        )

        response = self.client.get('/cars/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(response.json(),
                         [{'id': 2, 'milage': [], 'title': 'list test', 'descriptions': 'list test', 'owner': None}]
                         )
