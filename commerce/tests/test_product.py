from django.contrib.auth.models import User
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_204_NO_CONTENT,
)
from rest_framework.test import APITestCase
from commerce.models import Category, Product, Tag


class ProductTests(APITestCase):
    def setUp(self):
        _ = Product.objects.create(title="product1", price=1)
        _ = Category.objects.create(title="category")
        _ = Tag.objects.create(title="tag")

    def test_list_product(self):
        response = self.client.get(
            "/commerce/products/", data=None, format="json"
        )

        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertEqual(response.data["count"], 1)

    def test_create_product(self):
        response = self.client.post(
            "/commerce/products/",
            data={
                "title": "product2",
                "category": "/commerce/categories/1/",
                "tag": ["/commerce/tags/1/"],
                "price": 2,
            },
            format="json",
        )

        self.assertEqual(response.status_code, HTTP_201_CREATED)
        self.assertEqual(Product.objects.all().count(), 2)

    def test_retrieve_product(self):
        response = self.client.get(
            "/commerce/products/1/", data=None, format="json"
        )

        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertEqual(response.data["price"], 1)

    def test_update_product(self):
        response = self.client.put(
            "/commerce/products/1/",
            data={
                "title": "product1",
                "category": "/commerce/categories/1/",
                "tag": ["/commerce/tags/1/"],
                "price": 1,
            },
            format="json",
        )

        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertEqual(
            response.data["category"],
            "http://testserver/commerce/categories/1/",
        )

    def test_destroy_product(self):
        response = self.client.delete(
            "/commerce/products/1/", data=None, format="json"
        )

        self.assertEqual(response.status_code, HTTP_204_NO_CONTENT)
        self.assertEqual(Product.objects.all().count(), 0)
