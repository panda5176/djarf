# Generated by Django 4.1.7 on 2023-03-30 11:09

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("commerce", "0010_alter_review_rating"),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name="cart",
            name="unique_customer_product",
        ),
        migrations.RemoveConstraint(
            model_name="order2product",
            name="unique_order_product",
        ),
        migrations.RemoveConstraint(
            model_name="review",
            name="unique_reviewer_product",
        ),
        migrations.RenameField(
            model_name="product",
            old_name="tag",
            new_name="tags",
        ),
        migrations.AddField(
            model_name="product",
            name="modified",
            field=models.DateTimeField(auto_now=True, db_index=True),
        ),
        migrations.RemoveField(
            model_name="product",
            name="dislikes",
        ),
        migrations.RemoveField(
            model_name="product",
            name="likes",
        ),
        migrations.RemoveField(
            model_name="review",
            name="dislikes",
        ),
        migrations.RemoveField(
            model_name="review",
            name="likes",
        ),
        migrations.AddConstraint(
            model_name="cart",
            constraint=models.UniqueConstraint(
                fields=("customer", "product"), name="cart_unique_customer_product"
            ),
        ),
        migrations.AddConstraint(
            model_name="order2product",
            constraint=models.UniqueConstraint(
                fields=("order", "product"), name="order2product_unique_order_product"
            ),
        ),
        migrations.AddConstraint(
            model_name="review",
            constraint=models.UniqueConstraint(
                fields=("reviewer", "product"), name="review_unique_reviewer_product"
            ),
        ),
        migrations.AddField(
            model_name="product",
            name="dislikes",
            field=models.ManyToManyField(
                blank=True, related_name="product_dislikes", to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddField(
            model_name="product",
            name="likes",
            field=models.ManyToManyField(
                blank=True, related_name="product_likes", to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddField(
            model_name="review",
            name="dislikes",
            field=models.ManyToManyField(
                blank=True, related_name="review_dislikes", to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddField(
            model_name="review",
            name="likes",
            field=models.ManyToManyField(
                blank=True, related_name="review_likes", to=settings.AUTH_USER_MODEL
            ),
        ),
    ]