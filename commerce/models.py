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

    def __str__(self):
        return ", ".join(
            [str(self.customer), str(self.product), str(self.created)]
        )

    class Meta:
        get_latest_by = "created"
        ordering = ["created"]
        indexes = [models.Index(fields=["customer", "product"])]
        constraints = [
            models.UniqueConstraint(
                fields=["customer", "product"],
                name="cart_unique_customer_product",
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

    def __str__(self):
        return ", ".join([str(self.customer), str(self.created)])

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

    def __str__(self):
        return ", ".join([str(self.order), str(self.product)])

    class Meta:
        ordering = ["order"]
        indexes = [models.Index(fields=["order", "product"])]
        constraints = [
            models.UniqueConstraint(
                fields=["order", "product"],
                name="order2product_unique_order_product",
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
    modified = models.DateTimeField(auto_now=True, db_index=True)
    price = models.PositiveIntegerField(db_index=True)
    description = models.TextField(default="", blank=True)

    def __str__(self):
        return self.title

    class Meta:
        get_latest_by = "created"
        ordering = ["-created"]


class ProductLike(models.Model):
    liker = models.ForeignKey(
        "auth.User", on_delete=models.CASCADE, related_name="product_likes"
    )
    product = models.ForeignKey(
        "Product", on_delete=models.CASCADE, related_name="product_likes"
    )

    def __str__(self):
        return ", ".join([str(self.liker), str(self.product)])

    class Meta:
        ordering = ["liker"]
        constraints = [
            models.UniqueConstraint(
                fields=["liker", "product"],
                name="product_like_unique_liker_product",
            )
        ]


class Review(models.Model):
    reviewer = models.ForeignKey(
        "auth.User", on_delete=models.CASCADE, related_name="reviews"
    )
    product = models.ForeignKey(
        "Product", on_delete=models.CASCADE, related_name="reviews"
    )
    rating = models.FloatField(
        db_index=True,
        choices=[(score / 2, score / 2) for score in range(1, 11)],
    )
    created = models.DateTimeField(auto_now_add=True, db_index=True)
    modified = models.DateTimeField(auto_now=True, db_index=True)
    description = models.TextField(default="", blank=True)

    def __str__(self):
        return ", ".join(
            [str(self.reviewer), str(self.product), str(self.rating)]
        )

    class Meta:
        get_latest_by = "created"
        ordering = ["-created"]
        constraints = [
            models.UniqueConstraint(
                fields=["reviewer", "product"],
                name="review_unique_reviewer_product",
            )
        ]


class ReviewLike(models.Model):
    liker = models.ForeignKey(
        "auth.User", on_delete=models.CASCADE, related_name="review_likes"
    )
    review = models.ForeignKey(
        "Review", on_delete=models.CASCADE, related_name="review_likes"
    )

    def __str__(self):
        return ", ".join([str(self.liker), str(self.review)])

    class Meta:
        ordering = ["liker"]
        constraints = [
            models.UniqueConstraint(
                fields=["liker", "review"],
                name="review_like_unique_liker_review",
            )
        ]


class Tag(models.Model):
    title = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["title"]
