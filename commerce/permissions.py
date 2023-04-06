from typing import Union
from rest_framework.permissions import BasePermission, IsAdminUser, SAFE_METHODS
from rest_framework.request import Request
from rest_framework.views import View
from commerce.models import Cart, Order, Order2Product, Product, Review


class IsAdminUserOrReadOnly(IsAdminUser):
    def has_permission(self, request: Request, view: View) -> bool:
        return (
            super().has_permission(request, view)
            or request.method in SAFE_METHODS
        )


class IsCustomer(BasePermission):
    def has_object_permission(
        self,
        request: Request,
        view: View,
        object: Union[Cart, Order, Order2Product],
    ) -> bool:
        if isinstance(object, Order2Product):
            return object.order.customer == request.user
        return object.customer == request.user


class IsReviewerOrReadOnly(BasePermission):
    def has_object_permission(
        self, request: Request, view: View, object: Review
    ) -> bool:
        return object.reviewer == request.user or request.method in SAFE_METHODS


class IsVendorOrReadOnly(BasePermission):
    def has_object_permission(
        self, request: Request, view: View, object: Product
    ) -> bool:
        return object.vendor == request.user or request.method in SAFE_METHODS
