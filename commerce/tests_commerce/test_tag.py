from rest_framework.status import (
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_204_NO_CONTENT,
)
from rest_framework.test import APITestCase
from commerce.models import Tag
from common.models import User


class TagTests(APITestCase):
    def setUp(self):
        user = User.objects.create(is_staff=True)
        self.client.force_authenticate(user=user)

        _ = Tag.objects.create(title="tag")

    def test_list_tag(self):
        response = self.client.get("/commerce/tags/", data=None, format="json")

        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertEqual(response.data["count"], 1)

    def test_create_tag(self):
        response = self.client.post(
            "/commerce/tags/",
            data={"title": "tag_created"},
            format="json",
        )

        self.assertEqual(response.status_code, HTTP_201_CREATED)
        self.assertEqual(Tag.objects.all().count(), 2)

    def test_retrieve_tag(self):
        response = self.client.get(
            "/commerce/tags/1/", data=None, format="json"
        )

        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertEqual(response.data["title"], "tag")

    def test_update_tag(self):
        response = self.client.put(
            "/commerce/tags/1/",
            data={"title": "tag_updated"},
            format="json",
        )

        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertEqual(response.data["title"], "tag_updated")

    def test_destroy_tag(self):
        response = self.client.delete(
            "/commerce/tags/1/", data=None, format="json"
        )

        self.assertEqual(response.status_code, HTTP_204_NO_CONTENT)
        self.assertEqual(Tag.objects.all().count(), 0)
