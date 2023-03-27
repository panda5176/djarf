from django.contrib.auth.models import User
from rest_framework.status import HTTP_200_OK
from rest_framework.test import APITestCase
from commerce.models import Category, Order, Order2Product, Product


class Order2ProductTests(APITestCase):
    def setUp(self):
        user = User.objects.create()
        category = Category.objects.create(title="category")
        order = Order.objects.create(customer=user)
        product = Product.objects.create(
            vendor=user, category=category, title="product1", price=1
        )
        Order2Product.objects.create(order=order, product=product, quantity=1)

    def test_list_order2project(self):
        response = self.client.get(
            "/commerce/order2products/", data=None, format="json"
        )

        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertEqual(response.data["count"], 1)

    def test_retrieve_order2project(self):
        response = self.client.get(
            "/commerce/order2products/1/", data=None, format="json"
        )

        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertEqual(response.data["quantity"], 1)
