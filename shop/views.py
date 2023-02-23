from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import Product


def index(request):
    context = {"latest_product_list": Product.objects.order_by("-date")[:10]}
    return render(request, "shop/index.html", context)


def hello(request):
    return HttpResponse("Hello, world!")


def detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, "shop/detail.html", {"product": product})


def like(request, product_id):
    return HttpResponse()
