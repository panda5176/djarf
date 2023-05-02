from django.http import HttpResponse, HttpRequest
from django.shortcuts import render


def index(request: HttpRequest) -> HttpResponse:
    return render(request, "index.html")


def room(request: HttpRequest, room_name: str) -> HttpResponse:
    return render(request, "room.html", {"room_name": room_name})
