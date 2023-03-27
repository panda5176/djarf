from django.db import models


class Cart(models.Model):
    customer = models.ForeignKey(
        "auth.User", on_delete=models.CASCADE, related_name="carts", unique=True
    )
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

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["title"]


class Comment(models.Model):
    commentor = models.ForeignKey(
        "auth.User", on_delete=models.CASCADE, related_name="comments"
    )
    product = models.ForeignKey(
        "Product", on_delete=models.CASCADE, related_name="comments"
    )
    rating = models.PositiveSmallIntegerField(
        db_index=True,
        choices=tuple(f for f in range(0.5, 5.01, 0.5)),
    )
    created = models.DateTimeField(auto_now_add=True, db_index=True)
    likes = models.PositiveSmallIntegerField(db_index=True, default=0)
    dislikes = models.PositiveSmallIntegerField(db_index=True, default=0)
    description = models.TextField(default="", blank=True)

    def __str__(self):
        return self.rating

    class Meta:
        get_latest_by = "created"
        ordering = ["-created"]


class Order(models.Model):
    customer = models.ForeignKey(
        "auth.User", on_delete=models.CASCADE, related_name="orders"
    )
    created = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        get_latest_by = "created"
        ordering = ["-created"]


class Order2Product(models.Model):
    order = models.ForeignKey(
        "Order", on_delete=models.CASCADE, related_name="order2products"
    )
    product = models.ForeignKey(
        "Product", on_delete=models.CASCADE, related_name="order2products"
    )
    quantity = models.PositiveSmallIntegerField(default=1)

    class Meta:
        ordering = ["order"]
        indexes = [models.Index(fields=["order", "product"])]
        constraints = [
            models.UniqueConstraint(
                fields=["order", "product"], name="unique_order_product"
            )
        ]


class Product(models.Model):
    vendor = models.ForeignKey(
        "auth.User", on_delete=models.CASCADE, related_name="products"
    )
    category = models.ForeignKey(
        "Category", on_delete=models.CASCADE, related_name="products"
    )
    tag = models.ManyToManyField("Tag", related_name="products", blank=True)
    title = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True, db_index=True)
    price = models.PositiveIntegerField(db_index=True)
    likes = models.PositiveSmallIntegerField(db_index=True, default=0)
    dislikes = models.PositiveSmallIntegerField(db_index=True, default=0)
    description = models.TextField(default="", blank=True)

    def __str__(self):
        return self.title

    class Meta:
        get_latest_by = "created"
        ordering = ["-created"]


class Tag(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["title"]
