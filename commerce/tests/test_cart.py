from django.contrib.auth.models import User
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_204_NO_CONTENT,
)
from rest_framework.test import APITestCase
from commerce.models import Cart, Category, Product


class CartTests(APITestCase):
    def setUp(self):
        user = User.objects.create()
        category = Category.objects.create(title="category")
        product1 = Product.objects.create(
            vendor=user, category=category, title="product1", price=1
        )
        _ = Product.objects.create(
            vendor=user, category=category, title="product2", price=2
        )

        _ = Cart.objects.create(customer=user, product=product1)

    def test_list_cart(self):
        response = self.client.get("/commerce/carts/", data=None, format="json")

        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertEqual(response.data["count"], 1)

    def test_create_cart(self):
        response = self.client.post(
            "/commerce/carts/",
            data={
                "customer": "/commerce/users/1/",
                "product": "/commerce/products/2/",
            },
            format="json",
        )

        self.assertEqual(response.status_code, HTTP_201_CREATED)
        self.assertEqual(Cart.objects.all().count(), 2)

    def test_retrieve_cart(self):
        response = self.client.get(
            "/commerce/carts/1/", data=None, format="json"
        )

        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertEqual(response.data["quantity"], 1)

    def test_update_cart(self):
        response = self.client.put(
            "/commerce/carts/1/",
            data={
                "customer": "/commerce/users/1/",
                "product": "/commerce/products/1/",
                "quantity": 2,
            },
            format="json",
        )

        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertEqual(response.data["quantity"], 2)

    def test_destroy_cart(self):
        response = self.client.delete(
            "/commerce/carts/1/", data=None, format="json"
        )

        self.assertEqual(response.status_code, HTTP_204_NO_CONTENT)
        self.assertEqual(Cart.objects.all().count(), 0)
