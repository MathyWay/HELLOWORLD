from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello mthfckr")


def about(request):
    return HttpResponse("<h2>Главная<О сайте>")


def contact(request):
    return HttpResponse("<h2>Контакты<h2>")