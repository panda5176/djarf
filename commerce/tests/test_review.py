from django.contrib.auth.models import User
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_204_NO_CONTENT,
)
from rest_framework.test import APITestCase
from commerce.models import Category, Product, Review


class ProductTests(APITestCase):
    def setUp(self):
        user = User.objects.create()
        category = Category.objects.create(title="category")
        product = Product.objects.create(
            vendor=user, category=category, title="product1", price=1
        )
        _ = Product.objects.create(
            vendor=user, category=category, title="product2", price=2
        )
        _ = Review.objects.create(reviewer=user, product=product, rating=5.0)

    def test_list_review(self):
        response = self.client.get(
            "/commerce/reviews/", data=None, format="json"
        )

        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertEqual(response.data["count"], 1)

    def test_create_review(self):
        response = self.client.post(
            "/commerce/reviews/",
            data={
                "reviewer": "/commerce/users/1/",
                "product": "/commerce/products/2/",
                "rating": 0.5,
            },
            format="json",
        )

        print(response.data)
        self.assertEqual(response.status_code, HTTP_201_CREATED)
        self.assertEqual(Review.objects.all().count(), 2)

    def test_retrieve_review(self):
        response = self.client.get(
            "/commerce/reviews/1/", data=None, format="json"
        )

        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertEqual(response.data["rating"], 5.0)

    def test_update_review(self):
        response = self.client.put(
            "/commerce/reviews/1/",
            data={
                "reviewer": "/commerce/users/1/",
                "product": "/commerce/products/1/",
                "rating": 0.5,
            },
            format="json",
        )

        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertEqual(response.data["rating"], 0.5)

    def test_destroy_review(self):
        response = self.client.delete(
            "/commerce/reviews/1/", data=None, format="json"
        )

        self.assertEqual(response.status_code, HTTP_204_NO_CONTENT)
        self.assertEqual(Review.objects.all().count(), 0)
