import logging
from rest_framework.permissions import IsAdminUser
from rest_framework.viewsets import ModelViewSet
from common.models import User
from common.permissions import IsOwnerOrReadOnly
from common.serializers import UserSerializer, UserAdminSerializer

LOGGER = logging.getLogger(__name__)


class UserAdminViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserAdminSerializer
    permission_classes = [IsAdminUser]


class UserViewSet(UserAdminViewSet):
    serializer_class = UserSerializer
    permission_classes = [IsOwnerOrReadOnly]
