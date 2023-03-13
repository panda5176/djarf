from rest_framework import serializers
from commerce.models import Cart, Category, Order, Product, Tag


class CartSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cart
        fields = "__all__"
