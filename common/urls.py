from django.urls import path, include
from rest_framework.routers import DefaultRouter
from common.views import UserViewSet, UserAdminViewSet

router = DefaultRouter()
router.register("users", UserViewSet, basename="user")
router.register("users-admin", UserAdminViewSet, basename="user_admin")


urlpatterns = [
    path("", include(router.urls)),
]
