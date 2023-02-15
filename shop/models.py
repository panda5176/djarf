from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=50)
    like = models.IntegerField(default=0)


class Comment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    date = models.DateTimeField("date published")
