from django.shortcuts import render
from django.http import HttpRequest


def say_my_name(request: HttpRequest, name: str):
    return render(request, "index.html", context=dict(name=name))


def jackson_view(request: HttpRequest):
    return say_my_name(request, "jackson")


def pedro_view(request: HttpRequest):
    return say_my_name(request, "pedro")
