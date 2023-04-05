from rest_framework.permissions import BasePermission, SAFE_METHODS
from rest_framework.request import Request
from rest_framework.views import View
from common.models import User


class IsOwnerOrReadOnly(BasePermission):
    def has_object_permission(
        self, request: Request, view: View, object: User
    ) -> bool:
        return object == request.user or request.method in SAFE_METHODS
