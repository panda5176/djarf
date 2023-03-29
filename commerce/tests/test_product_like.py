from django.contrib.auth.models import User
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_204_NO_CONTENT,
)
from rest_framework.test import APITestCase
from commerce.models import Category, Product, ProductLike


class ProductLikeTests(APITestCase):
    def setUp(self):
        user1 = User.objects.create(username="user1")
        _ = User.objects.create(username="user2")
        category = Category.objects.create(title="category")
        product = Product.objects.create(
            vendor=user1, category=category, title="product1", price=1
        )
        _ = ProductLike.objects.create(liker=user1, product=product)

    def test_list_product_like(self):
        response = self.client.get(
            "/commerce/product_likes/", data=None, format="json"
        )

        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertEqual(response.data["count"], 1)

    def test_create_product_like(self):
        response = self.client.post(
            "/commerce/product_likes/",
            data={
                "liker": "/commerce/users/2/",
                "product": "/commerce/products/1/",
            },
            format="json",
        )

        self.assertEqual(response.status_code, HTTP_201_CREATED)
        self.assertEqual(ProductLike.objects.all().count(), 2)

    def test_retrieve_product_like(self):
        response = self.client.get(
            "/commerce/product_likes/1/", data=None, format="json"
        )

        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertEqual(
            response.data["liker"], "http://testserver/commerce/users/1/"
        )

    def test_destroy_product_like(self):
        response = self.client.delete(
            "/commerce/product_likes/1/", data=None, format="json"
        )

        self.assertEqual(response.status_code, HTTP_204_NO_CONTENT)
        self.assertEqual(ProductLike.objects.all().count(), 0)
