from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from commerce.models import Cart, Category, Order, Order2Product, Product, Tag
from commerce.serializers import (
    UserSerializer,
    CartSerializer,
    CategorySerializer,
    OrderSerializer,
    Order2ProductSerializer,
    ProductSerializer,
    TagSerializer,
)


@api_view(["GET"])
def api_root(request, format=None):
    return Response(
        {"users": reverse("user-list", request=request, format=format)},
        {"carts": reverse("cart-list", request=request, format=format)},
        {
            "categories": reverse(
                "category-list", request=request, format=format
            )
        },
        {"orders": reverse("order-list", request=request, format=format)},
        {"products": reverse("product-list", request=request, format=format)},
        {"tags": reverse("tag-list", request=request, format=format)},
    )


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
        if self.action == "create":
            return User.objects.all()
        return super().get_queryset()


class Order2ProductViewSet(ReadOnlyModelViewSet):
    queryset = Order2Product.objects.all()
    serializer_class = Order2ProductSerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class TagViewSet(ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
