from django.urls import path, include
from rest_framework.routers import DefaultRouter
from commerce.views import (
    UserViewSet,
    CartViewSet,
    CartAdminViewSet,
    CategoryViewSet,
    OrderViewSet,
    OrderAdminViewSet,
    Order2ProductViewSet,
    Order2ProductAdminViewSet,
    ProductViewSet,
    ProductAdminViewSet,
    ReviewViewSet,
    ReviewAdminViewSet,
    TagViewSet,
)

router = DefaultRouter()
router.register("users", UserViewSet, basename="commerce.user")
router.register("carts", CartViewSet, basename="cart")
router.register("categories", CategoryViewSet, basename="category")
router.register("orders", OrderViewSet, basename="order")
router.register(
    "order2products", Order2ProductViewSet, basename="order2product"
)
router.register("products", ProductViewSet, basename="product")
router.register("reviews", ReviewViewSet, basename="review")
router.register("tags", TagViewSet, basename="tag")
router.register("carts-admin", CartAdminViewSet, basename="cart_admin")
router.register("orders-admin", OrderAdminViewSet, basename="order_admin")
router.register(
    "order2products-admin",
    Order2ProductAdminViewSet,
    basename="order2product_admin",
)
router.register("products-admin", ProductAdminViewSet, basename="product_admin")
router.register("reviews-admin", ReviewAdminViewSet, basename="review_admin")


urlpatterns = [
    path("", include(router.urls)),
]
