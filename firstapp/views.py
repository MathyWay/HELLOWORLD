from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello mthfckr")


def about(request):
    return HttpResponse("<h2>Главная<О сайте>")


def contact(request):
    return HttpResponse("<h2>Контакты</h2>")


def product(request, productid):
    output = "<h2>Product № {0}</h2>".format(productid)
    return HttpResponse(output)


def users(request, id, name):
    output = "<h2></h2>User<h3>id: {0}  name: {1}</h3>".format(id, name)
    return HttpResponse(output)
