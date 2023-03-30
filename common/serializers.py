import logging
from rest_framework.serializers import HyperlinkedModelSerializer
from common.models import User

LOGGER = logging.getLogger(__name__)


class UserSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = [
            "url",
            "id",
            "created",
            "updated",
            "username",
            "first_name",
            "last_name",
            "email",
            "password",
            "groups",
            # "user_permissions",
            "is_staff",
            "is_active",
            "is_superuser",
            "last_login",
            "date_joined",
        ]
        read_only_fields = ["created", "updated"]
