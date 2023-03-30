import logging
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from commerce.models import (
    Cart,
    Category,
    Order,
    Order2Product,
    Product,
    Review,
    Tag,
)
from commerce.serializers import (
    UserSerializer,
    CartSerializer,
    CategorySerializer,
    OrderSerializer,
    Order2ProductSerializer,
    ProductSerializer,
    ReviewSerializer,
    TagSerializer,
)
from common.models import User

LOGGER = logging.getLogger(__name__)


class UserViewSet(ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CartViewSet(ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get_queryset(self):
        """Overriding to pass User for request data to Order view."""
        if self.action == "create":
            return User.objects.all()
        return super().get_queryset()


class Order2ProductViewSet(ReadOnlyModelViewSet):
    queryset = Order2Product.objects.all()
    serializer_class = Order2ProductSerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ReviewViewSet(ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class TagViewSet(ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
