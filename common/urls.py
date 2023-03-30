from django.urls import path, include
from rest_framework.routers import DefaultRouter
from common.views import UserViewSet

router = DefaultRouter()
router.register("users", UserViewSet, basename="user")


urlpatterns = [
    path("", include(router.urls)),
    path("api-auth/", include("rest_framework.urls")),
]
