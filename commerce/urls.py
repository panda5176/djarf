from django.urls import path, include
from rest_framework.routers import DefaultRouter
from commerce.views import (
    CartViewSet,
    CategoryViewSet,
    OrderViewSet,
    ProductViewSet,
    TagViewSet,
)

router = DefaultRouter()
router.register("carts", CartViewSet, basename="cart")
router.register("categories", CategoryViewSet, basename="category")
router.register("orders", OrderViewSet, basename="order")
router.register("products", ProductViewSet, basename="product")
router.register("tags", TagViewSet, basename="tag")

urlpatterns = [
    path("", include(router.urls)),
]
