import logging
from django.contrib.auth.models import User
from rest_framework.serializers import HyperlinkedModelSerializer, IntegerField
from commerce.models import (
    Cart,
    Category,
    Order,
    Order2Product,
    Product,
    Review,
    Tag,
)

LOGGER = logging.getLogger(__name__)


class UserSerializer(HyperlinkedModelSerializer):
    orders_count = IntegerField(source="orders.count", read_only=True)
    products_count = IntegerField(source="products.count", read_only=True)
    reviews_count = IntegerField(source="reviews.count", read_only=True)

    class Meta:
        model = User
        fields = [
            "url",
            "id",
            "carts",
            "orders_count",
            "orders",
            "products_count",
            "products",
            "product_likes",
            "reviews_count",
            "reviews",
            "review_likes",
        ]
        read_only_fields = [
            "carts",
            "orders_count",
            "orders",
            "products_count",
            "products",
            "product_likes",
            "reviews_count",
            "reviews",
            "review_likes",
        ]


class CartSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Cart
        fields = [
            "url",
            "id",
            "created",
            "updated",
            "customer",
            "product",
            "quantity",
        ]
        read_only_fields = ["created", "updated"]


class CategorySerializer(HyperlinkedModelSerializer):
    products_count = IntegerField(source="products.count", read_only=True)

    class Meta:
        model = Category
        fields = [
            "url",
            "id",
            "created",
            "updated",
            "title",
            "products_count",
            "products",
        ]
        read_only_fields = ["created", "updated", "products_count", "products"]


class OrderSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Order
        fields = [
            "url",
            "id",
            "created",
            "updated",
            "customer",
            "order2products",
        ]
        read_only_fields = ["created", "updated", "order2products"]

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
        fields = [
            "url",
            "id",
            "created",
            "updated",
            "order",
            "product",
            "quantity",
        ]
        read_only_fields = ["created", "updated"]


class ProductSerializer(HyperlinkedModelSerializer):
    likes_count = IntegerField(source="likes.count", read_only=True)
    dislikes_count = IntegerField(source="dislikes.count", read_only=True)

    class Meta:
        model = Product
        fields = [
            "url",
            "id",
            "created",
            "updated",
            "vendor",
            "category",
            "tags",
            "likes",
            "likes_count",
            "dislikes",
            "dislikes_count",
            "title",
            "price",
            "description",
            "order2products",
            "reviews",
        ]
        read_only_fields = [
            "created",
            "updated",
            "likes_count",
            "dislikes_count",
            "order2products",
            "reviews",
        ]


class ReviewSerializer(HyperlinkedModelSerializer):
    likes_count = IntegerField(source="likes.count", read_only=True)
    dislikes_count = IntegerField(source="dislikes.count", read_only=True)

    class Meta:
        model = Review
        fields = [
            "url",
            "id",
            "created",
            "updated",
            "reviewer",
            "product",
            "likes",
            "likes_count",
            "dislikes",
            "dislikes_count",
            "rating",
            "description",
        ]
        read_only_fields = [
            "created",
            "updated",
            "likes_count",
            "dislikes_count",
        ]


class TagSerializer(HyperlinkedModelSerializer):
    products_count = IntegerField(source="products.count", read_only=True)

    class Meta:
        model = Tag
        fields = [
            "url",
            "id",
            "created",
            "updated",
            "title",
            "products_count",
            "products",
        ]
        read_only_fields = ["created", "updated", "products_count", "products"]
