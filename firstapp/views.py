from django.shortcuts import render
from django.http import HttpResponse
import sqlite3


def index(request):
    header = "Hello KATE and KIRA"  # обычная переменная
    langs = ["English", "German", "Spanish"]  # массив
    user = {"name": "Tom", "age": 23}  # словарь
    addr = ("Абрикосовая", 23, 45)  # кортеж

    data = {"header": header, "langs": langs, "user": user, "address": addr}
    return render(request, "index.html", context=data)


def about(request):
    return HttpResponse("<h2>Главная<О сайте>")


def contact(request):
    return HttpResponse("<h2>Контакты</h2>")


def product(request, productid):
    output = "<h2>Product № {0}</h2>".format(productid)
    return HttpResponse(output)


def init_users(request, name, age):
    con = sqlite3.connect("users.db")
    cur = con.cursor()
    cur.execute('INSERT INTO users values (?, ?)', (name, age))
    con.commit()
    con.close()
    output = str(name) + " age: {0} user added</h2>".format(age)
    return HttpResponse(output)


def show_users(request):
    con = sqlite3.connect("users.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    output = ''
    for i in cur.execute('SELECT * FROM users'):
        output += "Name: {0}, age: {1}  ".format(i['name'], i['age'])
    con.close()
    return HttpResponse(output)
