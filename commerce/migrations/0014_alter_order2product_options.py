# Generated by Django 4.1.7 on 2023-04-10 07:02

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("commerce", "0013_remove_product_dislikes_remove_product_likes_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="order2product",
            options={"get_latest_by": "created", "ordering": ["-created"]},
        ),
    ]
