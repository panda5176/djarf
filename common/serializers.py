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
        read_only_fields = ["created", "updated", "last_login", "date_joined"]

    def create(self, validated_data: dict) -> User:
        """Creates User with hashed password."""
        user: User = super().create(validated_data)
        user.set_password(validated_data["password"])
        user.save()
        return user

    def update(self, instance: User, validated_data: dict) -> User:
        """Updates User with hashed password."""
        user: User = super().update(instance, validated_data)
        user.set_password(validated_data["password"])
        user.save()
        return user
