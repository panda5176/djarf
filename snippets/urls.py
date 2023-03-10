from django.urls import path, include
from rest_framework.renderers import StaticHTMLRenderer
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views

urlpatterns = [
    path("", views.api_root),
    path(
        "snippets/",
        views.SnippetViewSet.as_view({"get": "list", "post": "create"}),
        name="snippet-list",
    ),
    path(
        "snippets/<int:pk>/",
        views.SnippetViewSet.as_view(
            {
                "get": "retrieve",
                "put": "update",
                "patch": "partial_update",
                "delete": "destroy",
            }
        ),
        name="snippet-detail",
    ),
    path(
        "snippets/<int:pk>/highlight/",
        views.SnippetViewSet.as_view(
            {"get": "highlight"}, renderer_classes=[StaticHTMLRenderer]
        ),
        name="snippet-highlight",
    ),
    path(
        "users/", views.UserViewSet.as_view({"get": "list"}), name="user-list"
    ),
    path(
        "users/<int:pk>/",
        views.UserViewSet.as_view({"get": "retrieve"}),
        name="user-detail",
    ),
]

urlpatterns = format_suffix_patterns(urlpatterns)

urlpatterns += [
    path("api-auth/", include("rest_framework.urls")),
]
