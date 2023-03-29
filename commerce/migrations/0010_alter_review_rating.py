# Generated by Django 4.1.7 on 2023-03-29 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("commerce", "0009_alter_review_product_alter_review_reviewer"),
    ]

    operations = [
        migrations.AlterField(
            model_name="review",
            name="rating",
            field=models.FloatField(
                choices=[
                    (0.5, 0.5),
                    (1.0, 1.0),
                    (1.5, 1.5),
                    (2.0, 2.0),
                    (2.5, 2.5),
                    (3.0, 3.0),
                    (3.5, 3.5),
                    (4.0, 4.0),
                    (4.5, 4.5),
                    (5.0, 5.0),
                ],
                db_index=True,
            ),
        ),
    ]