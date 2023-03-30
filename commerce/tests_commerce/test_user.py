from rest_framework.status import HTTP_200_OK
from rest_framework.test import APITestCase
from common.models import User


class UserTests(APITestCase):
    def setUp(self):
        _ = User.objects.create()

    def test_list_user(self):
        response = self.client.get("/common/users/", data=None, format="json")
        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertEqual(response.data["count"], 1)

    def test_retrieve_user(self):
        response = self.client.get("/common/users/1/", data=None, format="json")

        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertEqual(response.data["id"], 1)
