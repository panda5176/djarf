import logging
from django.contrib.auth.models import User
from rest_framework.serializers import HyperlinkedModelSerializer
from commerce.models import (
    Cart,
    Category,
    Order,
    Order2Product,
    Product,
    ProductLike,
    Review,
    ReviewLike,
    Tag,
)

LOGGER = logging.getLogger(__name__)


class UserSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = [
            "url",
            "id",
            "carts",
            "orders",
            "products",
            "product_likes",
            "reviews",
            "review_likes",
        ]
        read_only_fields = [
            "carts",
            "orders",
            "products",
            "product_likes",
            "reviews",
            "review_likes",
        ]


class CartSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Cart
        fields = ["url", "id", "customer", "product", "created", "quantity"]


class CategorySerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ["url", "id", "title", "products"]
        read_only_fields = ["products"]


class OrderSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Order
        fields = ["url", "id", "customer", "created", "order2products"]
        read_only_fields = ["order2products"]

    def create(self, validated_data) -> Order:
        """Creating Order creates Order2Products and deletes Cart.

        Creating Order from customer creates Order2Products from Cart items of \
            customer and deletes Cart.
        """
        order = Order.objects.create(**validated_data)
        customer: User = validated_data["customer"]
        for cart in customer.carts.all():
            Order2Product.objects.create(
                order=order, product=cart.product, quantity=cart.quantity
            )
            cart.delete()
        return order


class Order2ProductSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Order2Product
        fields = ["url", "id", "order", "product", "quantity"]


class ProductSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = [
            "url",
            "id",
            "vendor",
            "category",
            "tag",
            "title",
            "created",
            "modified",
            "price",
            "description",
            "order2products",
            "product_likes",
            "reviews",
        ]
        read_only_fields = ["order2products", "product_likes", "reviews"]


class ProductLikeSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = ProductLike
        fields = ["url", "id", "liker", "product"]


class ReviewSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Review
        fields = [
            "url",
            "id",
            "reviewer",
            "product",
            "rating",
            "created",
            "modified",
            "description",
            "review_likes",
        ]
        read_only_fields = ["review_likes"]


class ReviewLikeSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = ReviewLike
        fields = ["url", "id", "liker", "review"]


class TagSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Tag
        fields = ["url", "id", "title", "products"]
        read_only_fields = ["products"]
