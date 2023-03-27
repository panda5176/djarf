from django.contrib.auth.models import User
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_204_NO_CONTENT,
)
from rest_framework.test import APITestCase
from commerce.models import Cart, Category, Order, Order2Product, Product


class OrderTests(APITestCase):
    def setUp(self):
        user1 = User.objects.create(username="user1")
        user2 = User.objects.create(username="user2")
        user3 = User.objects.create(username="user3")
        category = Category.objects.create(title="category")
        product1 = Product.objects.create(
            vendor=user1, category=category, title="product1", price=1
        )
        product2 = Product.objects.create(
            vendor=user1, category=category, title="product2", price=2
        )

        order = Order.objects.create(customer=user2)
        Order2Product.objects.create(order=order, product=product1, quantity=1)
        Order2Product.objects.create(order=order, product=product2, quantity=2)

        Cart.objects.create(customer=user3, product=product1, quantity=2)
        Cart.objects.create(customer=user3, product=product2, quantity=3)

    def test_list_order(self):
        response = self.client.get(
            "/commerce/orders/", data=None, format="json"
        )

        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertEqual(response.data["count"], 1)

    def test_create_order(self):
        response = self.client.post(
            "/commerce/orders/",
            data={"customer": "/commerce/users/3/"},
            format="json",
        )

        self.assertEqual(response.status_code, HTTP_201_CREATED)
        self.assertEqual(Order.objects.all().count(), 2)
        self.assertEqual(Order2Product.objects.all().count(), 4)
        self.assertEqual(Cart.objects.all().count(), 0)

    def test_retrieve_order(self):
        response = self.client.get(
            "/commerce/orders/1/", data=None, format="json"
        )

        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertEqual(
            response.data["customer"], "http://testserver/commerce/users/2/"
        )

    def test_update_order(self):
        response = self.client.put(
            "/commerce/orders/1/",
            data={"customer": "/commerce/users/3/"},
            format="json",
        )

        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertEqual(
            response.data["customer"], "http://testserver/commerce/users/3/"
        )

    def test_destroy_order(self):
        response = self.client.delete(
            "/commerce/orders/1/", data=None, format="json"
        )

        self.assertEqual(response.status_code, HTTP_204_NO_CONTENT)
        self.assertEqual(Order.objects.all().count(), 0)
