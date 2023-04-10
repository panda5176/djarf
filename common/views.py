import logging
from rest_framework.permissions import IsAdminUser
from rest_framework.viewsets import ModelViewSet
from common.models import User
from common.permissions import IsOwnerOrReadOnly
from common.serializers import UserSerializer, UserAdminSerializer

LOGGER = logging.getLogger(__name__)


class UserAdminViewSet(ModelViewSet):
    """User viewset for admin.

    Model Attributes
    ----------------
    - `username`
    - `first_name`
    - `last_name`
    - `email`
    - `password`
    - `groups`
    - `user_permissions`
    - `is_staff`
    - `is_active`
    - `is_superuser`
    - `last_login`
    - `date_joined`

    Serializer Fields
    -----------------
    - `username`
    - `first_name`
    - `last_name`
    - `email`
    - `password`
    - `is_staff`
    - `is_active`
    - `is_superuser`
    - `last_login` read_only
    - `date_joined` read_only

    Permission
    ----------
    - Admin: Create / List / Retrieve / Update / Destroy
    """

    queryset = User.objects.all()
    serializer_class = UserAdminSerializer
    permission_classes = [IsAdminUser]


class UserViewSet(UserAdminViewSet):
    """User viewset for admin.

    Model Attributes
    ----------------
    - `username`
    - `first_name`
    - `last_name`
    - `email`
    - `password`
    - `groups`
    - `user_permissions`
    - `is_staff`
    - `is_active`
    - `is_superuser`
    - `last_login`
    - `date_joined`

    Serializer Fields
    -----------------
    - `username`
    - `first_name`
    - `last_name`
    - `email`
    - `password` write_only
    - `last_login` read_only
    - `date_joined` read_only

    Permission
    ----------
    - Owner: Create / List / Retrieve / Update / Destroy
    - Others: ~~Create~~ / List / Retrieve / ~~Update~~ / ~~Destroy~~
    """

    serializer_class = UserSerializer
    permission_classes = [IsOwnerOrReadOnly]
