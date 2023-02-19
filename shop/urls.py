from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("hello", views.hello, name="hello"),
    path("<int:product_id>", views.detail, name="detail"),
    path("<int:product_id>/like", views.like, name="like"),
]
