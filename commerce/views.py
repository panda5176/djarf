import logging
from django.contrib.auth.models import AnonymousUser
from rest_framework.permissions import IsAdminUser, IsAuthenticated
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
    CartAdminSerializer,
    CategorySerializer,
    OrderSerializer,
    OrderAdminSerializer,
    Order2ProductSerializer,
    ProductSerializer,
    ProductAdminSerializer,
    ReviewSerializer,
    ReviewAdminSerializer,
    TagSerializer,
)
from common.models import User

LOGGER = logging.getLogger(__name__)


class UserViewSet(ReadOnlyModelViewSet):
    """User viewset for read-only.

    Fields
    ------
    - `carts` read_only `True`
    - `orders_count` IntegerField source `orders.count` read_only `True`
    - `orders` read_only `True`
    - `products_count` IntegerField source `products.count` read_only `True`
    - `products` read_only `True`
    - `reviews_count` IntegerField source `reviews.count` read_only `True`
    - `reviews` read_only `True`

    Permission
    ----------
    - Authenticated: ~~Create~~ / List / Retrieve / ~~Update~~ / ~~Destroy~~
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


class CartAdminViewSet(ModelViewSet):
    """Cart viewset for admin.

    Fields
    ------
    - `customer`
    - `product`
    - `quantity`

    Permission
    ----------
    - Admin: Create / List / Retrieve / Update / Destroy
    """

    queryset = Cart.objects.all()
    serializer_class = CartAdminSerializer
    permission_classes = [IsAdminUser]


class CartViewSet(CartAdminViewSet):
    """Cart viewset.

    Fields
    ------
    - `customer` read_only `True`
    - `product`
    - `quantity`

    Permission
    ----------
    - Admin: Create / List / Retrieve / Update / Destroy
    - Customer: Create / List / Retrieve / Update / Destroy
    """

    serializer_class = CartSerializer
    permission_classes = [IsAdminUser | IsCustomer]

    def list(self, request: Request) -> Response:
        """Lists Cart of the customer who is request user."""
        if isinstance(request.user, AnonymousUser):
            queryset = Cart.objects.none()
        else:
            queryset = Cart.objects.filter(customer=request.user)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class CategoryViewSet(ModelViewSet):
    """Category viewset.

    Fields
    ------
    - `title`
    - `products_count` IntegerField source `products.count` read_only `True`
    - `products` read_only `True`

    Permission
    ----------
    - Admin: Create / List / Retrieve / Update / Destroy
    - Others: ~~Create~~ / List / Retrieve / ~~Update~~ / ~~Destroy~~
    """

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUserOrReadOnly]


class OrderAdminViewSet(ModelViewSet):
    """Order viewset for admin.

    Fields
    ------
    - `customer`
    - `order2products` read_only `True`

    Permission
    ----------
    - Admin: Create / List / Retrieve / Update / Destroy
    """

    queryset = Order.objects.all()
    serializer_class = OrderAdminSerializer
    permission_classes = [IsAdminUser]


class OrderViewSet(OrderAdminViewSet):
    """Order viewset.

    Fields
    ------
    - `customer` read_only `True`
    - `order2products` read_only `True`

    Permission
    ----------
    - Admin: Create / List / Retrieve / Update / Destroy
    - Customer: Create / List / Retrieve / Update / Destroy
    """

    serializer_class = OrderSerializer
    permission_classes = [IsAdminUser | IsCustomer]

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

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class Order2ProductAdminViewSet(ReadOnlyModelViewSet):
    """Order to Product quantity relationships viewset for admin.

    Fields
    ------
    - `order`
    - `product`
    - `quantity`

    Permission
    ----------
    - Admin: Create / List / Retrieve / Update / Destroy
    """

    queryset = Order2Product.objects.all()
    serializer_class = Order2ProductSerializer
    permission_classes = [IsAdminUser]


class Order2ProductViewSet(Order2ProductAdminViewSet):
    """Order to Product quantity relationships viewset.

    Fields
    ------
    - `order`
    - `product`
    - `quantity`

    Permission
    ----------
    - Admin: Create / List / Retrieve / Update / Destroy
    - Customer: Create / List / Retrieve / Update / Destroy
    """

    permission_classes = [IsAdminUser | IsCustomer]

    def list(self, request: Request) -> Response:
        """Lists Order2Product of the customer who is request user."""
        if isinstance(request.user, AnonymousUser):
            queryset = Order2Product.objects.none()
        else:
            queryset = Order2Product.objects.filter(
                order__customer=request.user
            )

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class ProductAdminViewSet(ModelViewSet):
    """Product viewset for admin.

    Fields
    ------
    - `vendor`
    - `category`
    - `tags`
    - `title`
    - `price`
    - `description`
    - `order2products` read_only `True`
    - `reviews` read_only `True`

    Permission
    ----------
    - Admin: Create / List / Retrieve / Update / Destroy
    """

    queryset = Product.objects.all()
    serializer_class = ProductAdminSerializer
    permission_classes = [IsAdminUser]


class ProductViewSet(ProductAdminViewSet):
    """Product viewset.

    Fields
    ------
    - `vendor` read_only `True`
    - `category`
    - `tags`
    - `title`
    - `price`
    - `description`
    - `order2products` read_only `True`
    - `reviews` read_only `True`

    Permission
    ----------
    - Admin: Create / List / Retrieve / Update / Destroy
    - Vendor: Create / List / Retrieve / Update / Destroy
    - Others: ~~Create~~ / List / Retrieve / ~~Update~~ / ~~Destroy~~
    """

    serializer_class = ProductSerializer
    permission_classes = [IsAdminUser | IsVendorOrReadOnly]


class ReviewAdminViewSet(ModelViewSet):
    """Review viewset for admin.

    Fields
    ------
    - `reviewer`
    - `product`
    - `rating`
    - `description`

    Permission
    ----------
    - Admin: Create / List / Retrieve / Update / Destroy
    """

    queryset = Review.objects.all()
    serializer_class = ReviewAdminSerializer
    permission_classes = [IsAdminUser]


class ReviewViewSet(ReviewAdminViewSet):
    """Review viewset.

    Fields
    ------
    - `reviewer` read_only `True`
    - `product`
    - `rating`
    - `description`

    Permission
    ----------
    - Admin: Create / List / Retrieve / Update / Destroy
    - Reviewer: Create / List / Retrieve / Update / Destroy
    - Others: ~~Create~~ / List / Retrieve / ~~Update~~ / ~~Destroy~~
    """

    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAdminUser | IsReviewerOrReadOnly]


class TagViewSet(ModelViewSet):
    """Tag viewset.

    Fields
    ------
    - `title`
    - `products_count` IntegerField source `products.count` read_only `True`
    - `products` read_only `True`

    Permission
    ----------
    - Admin: Create / List / Retrieve / Update / Destroy
    - Others: ~~Create~~ / List / Retrieve / ~~Update~~ / ~~Destroy~~
    """

    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [IsAdminUserOrReadOnly]
