from django.shortcuts import render
from django.http import HttpResponse

from .models import Product


def index(request):
    context = {"latest_product_list": Product.objects.order_by("-date")[:10]}
    return render(request, "shop/index.html", context)


def hello(request):
    return HttpResponse("Hello, world!")


def detail(request, product_id):
    return HttpResponse()


def like(request, product_id):
    return HttpResponse()
