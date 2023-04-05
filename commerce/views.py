import logging
from django.contrib.auth.models import AnonymousUser
from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly
from rest_framework.request import Request
from rest_framework.response import Response
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
from commerce.permissions import (
    IsAdminUserOrReadOnly,
    IsCustomer,
    IsReviewerOrReadOnly,
    IsVendorOrReadOnly,
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
    permission_classes = [IsAuthenticatedOrReadOnly]


class CartAdminViewSet(ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [IsAdminUser]


class CartViewSet(CartAdminViewSet):
    permission_classes = [IsCustomer]

    def list(self, request: Request) -> Response:
        """Lists Cart of the customer who is request user."""
        if isinstance(request.user, AnonymousUser):
            queryset = Cart.objects.none()
        else:
            queryset = Cart.objects.filter(customer=request.user)

        serializer = CartSerializer(
            queryset, many=True, context={"request": request}
        )
        return Response(serializer.data)


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUserOrReadOnly]


class OrderAdminViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAdminUser]


class OrderViewSet(OrderAdminViewSet):
    permission_classes = [IsCustomer]

    def get_queryset(self):
        """Overriding to pass User for request data to Order view."""
        if self.action == "create":
            return User.objects.all()
        return super().get_queryset()

    def list(self, request: Request) -> Response:
        """Lists Order of the customer who is request user."""
        if isinstance(request.user, AnonymousUser):
            queryset = Order.objects.none()
        else:
            queryset = Order.objects.filter(customer=request.user)

        serializer = OrderSerializer(
            queryset, many=True, context={"request": request}
        )
        return Response(serializer.data)


class Order2ProductAdminViewSet(ReadOnlyModelViewSet):
    queryset = Order2Product.objects.all()
    serializer_class = Order2ProductSerializer
    permission_classes = [IsAdminUser]


class Order2ProductViewSet(Order2ProductAdminViewSet):
    permission_classes = [IsCustomer]

    def list(self, request: Request) -> Response:
        """Lists Order2Product of the customer who is request user."""
        if isinstance(request.user, AnonymousUser):
            queryset = Order2Product.objects.none()
        else:
            queryset = Order2Product.objects.filter(
                order__customer=request.user
            )

        serializer = Order2ProductSerializer(
            queryset, many=True, context={"request": request}
        )
        return Response(serializer.data)


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsVendorOrReadOnly]


class ReviewViewSet(ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsReviewerOrReadOnly]


class TagViewSet(ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [IsAdminUserOrReadOnly]
