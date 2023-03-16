from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from commerce.models import Cart, Category, Order, Product, Tag
from commerce.serializers import (
    UserSerializer,
    CartSerializer,
    CategorySerializer,
    OrderSerializer,
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


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def create(self, request):
        # TODO: Order must starts from Cart
        pass


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
