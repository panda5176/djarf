from rest_framework.status import (
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_204_NO_CONTENT,
)
from rest_framework.test import APITestCase
from common.models import User


class UserTests(APITestCase):
    def setUp(self):
        user = User.objects.create(username="user1")
        self.client.force_authenticate(user=user)

    def test_list_user(self):
        response = self.client.get("/common/users/", data=None, format="json")
        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertEqual(response.data["count"], 1)

    def test_create_user(self):
        response = self.client.post(
            "/common/users/",
            data={"username": "user2", "password": "password"},
            format="json",
        )

        self.assertEqual(response.status_code, HTTP_201_CREATED)
        self.assertEqual(User.objects.all().count(), 2)

    def test_retrieve_user(self):
        response = self.client.get("/common/users/1/", data=None, format="json")

        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertEqual(response.data["id"], 1)

    def test_update_user(self):
        response = self.client.put(
            "/common/users/1/",
            data={
                "username": "user2",
                "password": "password",
                "email": "mail@mail.mail",
            },
            format="json",
        )

        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertEqual(response.data["email"], "mail@mail.mail")

    def test_destroy_user(self):
        response = self.client.delete(
            "/common/users/1/", data=None, format="json"
        )

        self.assertEqual(response.status_code, HTTP_204_NO_CONTENT)
        self.assertEqual(User.objects.all().count(), 0)
