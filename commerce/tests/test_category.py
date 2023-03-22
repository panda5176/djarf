from rest_framework.status import (
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_204_NO_CONTENT,
)
from rest_framework.test import APITestCase
from commerce.models import Category


class CategoryTests(APITestCase):
    def setUp(self):
        _ = Category.objects.create(title="category")

    def test_list_category(self):
        response = self.client.get(
            "/commerce/categories/", data=None, format="json"
        )

        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertEqual(response.data["count"], 1)

    def test_create_category(self):
        response = self.client.post(
            "/commerce/categories/",
            data={"title": "category_created"},
            format="json",
        )

        self.assertEqual(response.status_code, HTTP_201_CREATED)
        self.assertEqual(Category.objects.all().count(), 2)

    def test_retrieve_category(self):
        response = self.client.get(
            "/commerce/categories/1/", data=None, format="json"
        )

        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertEqual(response.data["title"], "category")

    def test_update_category(self):
        response = self.client.put(
            "/commerce/categories/1/",
            data={"title": "category_updated"},
            format="json",
        )

        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertEqual(response.data["title"], "category_updated")

    def test_destroy_category(self):
        response = self.client.delete(
            "/commerce/categories/1/", data=None, format="json"
        )

        self.assertEqual(response.status_code, HTTP_204_NO_CONTENT)
        self.assertEqual(Category.objects.all().count(), 0)
