from rest_framework.test import APITestCase
from . import models


class TestAmenities(APITestCase):

    NAME = "Amenity Test"
    DESC = "Amenity Des"
    URL = "/api/v1/rooms/amenities/"

    def setUp(self):
        models.Amenity.objects.create(
            name=self.NAME,
            description=self.DESC,
        )

    def test_all_Amenities(self):

        response = self.client.get(self.URL)
        data = response.json()

        self.assertEqual(
            response.status_code,
            200,
            "Status code isn't 200.",
        )
        self.assertIsInstance(
            data,
            list,
        )
        self.assertEqual(
            len(data),
            1,
        )
        self.assertEqual(
            data[0]["name"],
            self.NAME,
        )
        self.assertEqual(
            data[0]["description"],
            self.DESC,
        )

    def test_create_amenity(self):

        NEW_NAME = "Amenity Test"
        NEW_DESC = "Amenity Des"

        response = self.client.post(
            self.URL,
            data={"name": "New Amenity", "description": "New Amenity desc."},
        )
        data = response.json()
        self.assertEqual(response.status_code, 200, "Not 200 status code")
        self.assertEqual(
            data["name"],
            NEW_NAME,
        )
        self.assertEqual(
            data["description"],
            NEW_DESC,
        )
        response = self.client.post(self.URL)
        data = response.json()
        self.assertEqual(response.status_code, 400)
        self.assertIn("name", data)
