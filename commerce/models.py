from django.db import models
from common.models import AbstractModel


class Cart(AbstractModel):
    """Cart to product quantity model.

    Attributes
    ----------
    - `customer` ForeignKey to `common.User`
    - `product` ForeignKey to `Product`
    - `quantity` PositiveSmallIntegerField default `1`

    Meta
    ----
    - get_latest_by `created`
    - ordering [`created`]
    - indexes [`customer`, `product`]
    - constraints `cart_unique_customer_product` UniqueConstraint \
        [`customer`, `product`]
    """

    customer = models.ForeignKey(
        "common.User", on_delete=models.CASCADE, related_name="carts"
    )
    product = models.ForeignKey(
        "Product", on_delete=models.CASCADE, related_name="carts"
    )
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


class Category(AbstractModel):
    """Category model.

    Attributes
    ----------
    - `title` CharField max_length `20` unique `True`

    Meta
    ----
    - ordering [`title`]
    """

    title = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["title"]


class Order(AbstractModel):
    """Order model.

    Attributes
    ----------
    - `customer` ForeignKey to `common.User`

    Meta
    ----
    - get_latest_by `created`
    - ordering [`-created`]
    """

    customer = models.ForeignKey(
        "common.User", on_delete=models.CASCADE, related_name="orders"
    )

    def __str__(self):
        return ", ".join([str(self.customer), str(self.created)])

    class Meta:
        get_latest_by = "created"
        ordering = ["-created"]


class Order2Product(AbstractModel):
    """Order to Product quantity relationships model.

    Attributes
    ----------
    - `order` ForeignKey to `Order`
    - `product` ForeignKey to `Product`
    - `quantity` PositiveSmallIntegerField default `1`

    Meta
    ----
    - get_latest_by `created`
    - ordering [`-created`]
    - indexes [`order`, `product`]
    - constraints `order2product_unique_order_product` UniqueConstraint \
        [`order`, `product`]
    """

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
        get_latest_by = "created"
        ordering = ["-created"]
        indexes = [models.Index(fields=["order", "product"])]
        constraints = [
            models.UniqueConstraint(
                fields=["order", "product"],
                name="order2product_unique_order_product",
            )
        ]


class Product(AbstractModel):
    """Product model.

    Attributes
    ----------
    - `vendor` ForeignKey to `common.User`
    - `category` ForeignKey to `Category`
    - `tags` ManyToManyField to `Tag` blank `True`
    - `title` CharField max_length `100`
    - `price` PositiveIntegerField db_index `True`
    - `description` TextField default `""` blank `True`

    Meta
    ----
    - get_latest_by `created`
    - ordering [`-created`]
    """

    vendor = models.ForeignKey(
        "common.User", on_delete=models.CASCADE, related_name="products"
    )
    category = models.ForeignKey(
        "Category", on_delete=models.CASCADE, related_name="products"
    )
    tags = models.ManyToManyField("Tag", related_name="products", blank=True)
    title = models.CharField(max_length=100)
    price = models.PositiveIntegerField(db_index=True)
    description = models.TextField(default="", blank=True)

    def __str__(self):
        return self.title

    class Meta:
        get_latest_by = "created"
        ordering = ["-created"]


class Review(AbstractModel):
    """Review model.

    Attributes
    ----------
    - `reviewer` ForeignKey to `common.User`
    - `product` ForeignKey to `Product`
    - `rating` FloatField db_index `True` choices `[0.5, 1.0, ..., 5.0]`
    - `description` TextField default `""` blank `True`

    Meta
    ----
    - get_latest_by `created`
    - ordering [`-created`]
    - constraints `review_unique_reviewer_product` UniqueConstraint \
        [`reviewer`, `product`]
    """

    reviewer = models.ForeignKey(
        "common.User", on_delete=models.CASCADE, related_name="reviews"
    )
    product = models.ForeignKey(
        "Product", on_delete=models.CASCADE, related_name="reviews"
    )
    rating = models.FloatField(
        db_index=True,
        choices=[(score / 2, score / 2) for score in range(1, 11)],
    )
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


class Tag(AbstractModel):
    """Tag model.

    Attributes
    ----------
    - `title` CharField max_length `20` unique `True`

    Meta
    ----
    - ordering [`title`]
    """

    title = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["title"]
