import logging
from rest_framework.viewsets import ModelViewSet
from common.models import User
from common.serializers import UserSerializer

LOGGER = logging.getLogger(__name__)


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
