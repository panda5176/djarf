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
from common.models import User


class UserSerializer(HyperlinkedModelSerializer):
    orders_count = IntegerField(source="orders.count", read_only=True)
    products_count = IntegerField(source="products.count", read_only=True)
    reviews_count = IntegerField(source="reviews.count", read_only=True)

    class Meta:
        model = User
        fields = [
            "url",
            "id",
            "created",
            "updated",
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
            "created",
            "updated",
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


class CartAdminSerializer(HyperlinkedModelSerializer):
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


class CartSerializer(CartAdminSerializer):
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
        read_only_fields = ["created", "updated", "customer"]

    def create(self, validated_data: dict) -> Cart:
        """Creates Cart with request user as customer."""
        validated_data["customer"] = self.context["request"].user
        cart: Cart = super().create(validated_data)
        cart.save()
        return cart


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


class OrderAdminSerializer(HyperlinkedModelSerializer):
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

    def create(self, validated_data: dict) -> Order:
        """Creates Order creating Order2Products and deleting Cart.

        Creates Order from customer creating Order2Products from Cart items of \
            customer and deleting Cart.
        """
        order = super().create(validated_data)
        customer: User = validated_data["customer"]
        for cart in customer.carts.all():
            Order2Product.objects.create(
                order=order, product=cart.product, quantity=cart.quantity
            )
            cart.delete()
        return order


class OrderSerializer(OrderAdminSerializer):
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
        read_only_fields = ["created", "updated", "customer", "order2products"]

    def create(self, validated_data: dict) -> Order:
        """Creates Order creating Order2Products and deleting Cart.

        Creates Order from customer creating Order2Products from Cart items of \
            customer and deleting Cart.
        Creates Order with request user as customer.
        """
        validated_data["customer"] = self.context["request"].user
        return super().create(validated_data)


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


class ProductAdminSerializer(HyperlinkedModelSerializer):
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


class ProductSerializer(ProductAdminSerializer):
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
            "vendor",
            "likes",
            "likes_count",
            "dislikes",
            "dislikes_count",
            "order2products",
            "reviews",
        ]

    def create(self, validated_data: dict) -> Product:
        """Creates Product with request user as vendor."""
        validated_data["vendor"] = self.context["request"].user
        product: Product = super().create(validated_data)
        product.save()
        return product


class ReviewAdminSerializer(HyperlinkedModelSerializer):
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


class ReviewSerializer(ReviewAdminSerializer):
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
            "reviewer",
            "likes",
            "likes_count",
            "dislikes",
            "dislikes_count",
        ]

    def create(self, validated_data: dict) -> Review:
        """Creates Review with request user as reviewer."""
        validated_data["reviewer"] = self.context["request"].user
        review: Review = super().create(validated_data)
        review.save()
        return review


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
