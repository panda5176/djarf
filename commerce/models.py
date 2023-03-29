from django.db import models


class Cart(models.Model):
    customer = models.ForeignKey(
        "auth.User", on_delete=models.CASCADE, related_name="carts"
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
    title = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["title"]


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


class Review(models.Model):
    reviewer = models.ForeignKey(
        "auth.User", on_delete=models.CASCADE, related_name="reviews"
    )
    product = models.ForeignKey(
        "Product", on_delete=models.CASCADE, related_name="reviews"
    )
    rating = models.DecimalField(
        max_digits=2,
        decimal_places=1,
        db_index=True,
        choices=[(score / 2, score / 2) for score in range(1, 11)],
    )
    created = models.DateTimeField(auto_now_add=True, db_index=True)
    modified = models.DateTimeField(auto_now=True, db_index=True)
    likes = models.PositiveSmallIntegerField(db_index=True, default=0)
    dislikes = models.PositiveSmallIntegerField(db_index=True, default=0)
    description = models.TextField(default="", blank=True)

    def __str__(self):
        return self.rating

    class Meta:
        get_latest_by = "created"
        ordering = ["-created"]
        constraints = [
            models.UniqueConstraint(
                fields=["reviewer", "product"], name="unique_reviewer_product"
            )
        ]


class Tag(models.Model):
    title = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["title"]
