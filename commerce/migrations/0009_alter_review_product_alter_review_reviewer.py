# Generated by Django 4.1.7 on 2023-03-29 12:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("commerce", "0008_alter_order_options_alter_category_title_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="review",
            name="product",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="reviews",
                to="commerce.product",
            ),
        ),
        migrations.AlterField(
            model_name="review",
            name="reviewer",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="reviews",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]