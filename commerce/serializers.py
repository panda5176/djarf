from django.contrib.auth.models import User
from rest_framework.serializers import HyperlinkedModelSerializer
from commerce.models import Cart, Category, Order, Order2Product, Product, Tag


class UserSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["url", "id", "carts", "orders"]


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
        fields = ["url", "id", "customer", "created"]
        read_only_fields = ["order2products"]

    def create(self, validated_data):
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
        fields = ["url", "id", "category", "tag", "title", "created", "price"]


class TagSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Tag
        fields = ["url", "id", "title", "products"]
        read_only_fields = ["products"]
