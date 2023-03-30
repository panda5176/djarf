from django.db import models
from django.contrib.auth.models import AbstractUser


class AbstractModel(models.Model):
    created = models.DateTimeField(auto_now_add=True, db_index=True)
    updated = models.DateTimeField(auto_now=True, db_index=True)

    class Meta:
        abstract = True


class User(AbstractUser, AbstractModel):
    class Meta:
        get_latest_by = "created"
        ordering = ["created"]
