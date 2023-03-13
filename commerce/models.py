from django.db import models


class Cart(models.Model):
    customer = models.OneToOneField("auth.User", on_delete=models.CASCADE)
    product = models.ForeignKey(
        "Product", on_delete=models.CASCADE, related_name="carts"
    )
    created = models.DateTimeField(auto_now_add=True, db_index=True)
    quantity = models.PositiveSmallIntegerField(default=1)

    class Meta:
        get_latest_by = "created"
        ordering = ["created"]
        indexes = [models.Index(fields=["customer", "product"])]
        constraints = [
            models.UniqueConstraint(
                fields=["customer", "product"], name="unique_customer_product"
            )
        ]


class Category(models.Model):
    title = models.CharField(max_length=20)

    class Meta:
        ordering = ["title"]


class Order(models.Model):
    customer = models.ForeignKey(
        "auth.User", on_delete=models.SET_NULL, related_name="orders", null=True
    )
    created = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        get_latest_by = "created"
        ordering = ["created"]


class Order2Product(models.Model):
    order = models.ForeignKey(
        "Order", on_delete=models.CASCADE, related_name="order2products"
    )
    quantity = models.PositiveSmallIntegerField(default=1)


class Product(models.Model):
    category = models.ForeignKey(
        "Category",
        on_delete=models.SET_NULL,
        related_name="products",
        null=True,
    )
    title = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True, db_index=True)
    price = models.PositiveIntegerField(db_index=True)

    class Meta:
        get_latest_by = "created"
        ordering = ["-created"]


class Tag(models.Model):
    title = models.CharField(max_length=20)

    class Meta:
        ordering = ["title"]
