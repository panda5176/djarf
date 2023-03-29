from django.urls import path, include
from rest_framework.routers import DefaultRouter
from commerce.views import (
    UserViewSet,
    CartViewSet,
    CategoryViewSet,
    OrderViewSet,
    Order2ProductViewSet,
    ProductViewSet,
    ProductLikeViewSet,
    ReviewViewSet,
    ReviewLikeViewSet,
    TagViewSet,
)

router = DefaultRouter()
router.register("users", UserViewSet, basename="user")
router.register("carts", CartViewSet, basename="cart")
router.register("categories", CategoryViewSet, basename="category")
router.register("orders", OrderViewSet, basename="order")
router.register(
    "order2products", Order2ProductViewSet, basename="order2product"
)
router.register("products", ProductViewSet, basename="product")
router.register("product_likes", ProductLikeViewSet, basename="productlike")
router.register("reviews", ReviewViewSet, basename="review")
router.register("review_likes", ReviewLikeViewSet, basename="reviewlike")
router.register("tags", TagViewSet, basename="tag")


urlpatterns = [
    path("", include(router.urls)),
]
