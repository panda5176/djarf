from django.db import models
from django.contrib.auth.models import AbstractUser


class AbstractModel(models.Model):
    """Abstract model for all models inheritance.

    Attributes
    ----------
    - `created` DateTimeField auto_now_add `True` db_index `True`
    - `updated` DateTimeField auto_now `True` db_index `True`
    """

    created = models.DateTimeField(auto_now_add=True, db_index=True)
    updated = models.DateTimeField(auto_now=True, db_index=True)

    class Meta:
        abstract = True


class User(AbstractUser, AbstractModel):
    """User model for all applications.

    Attributes
    ----------
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

    Meta
    ----
    - get_latest_by `created`
    - ordering [`created`]
    """

    class Meta:
        get_latest_by = "created"
        ordering = ["created"]
