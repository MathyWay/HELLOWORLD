from django.shortcuts import render
from django.http import HttpResponse
from dbwork import UserCl, DataBase, BASE_NAME


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


def init_users(request, ids, name, age):
    user = UserCl(int(ids), name, int(age))
    base = DataBase(BASE_NAME)
    base.init_data_base()
    base.init_user(user)
    output = str(name) + " age: {0} with id {1} user added</h2>".format(age, ids)
    return HttpResponse(output)


def search_form(request):
    return render(request, 'search_form.html')


def search(request):
    if 'q' in request.GET and request.GET['q'] and 'type' in request.GET and request.GET['type']:
        q = request.GET['q']
        types = request.GET['type']
        users = DataBase(BASE_NAME).take_users(types, q)
        if type(users) == UserCl:
            return render(request, 'search_results.html',
                          {'users': users, 'query': q})
        elif type(users) == list:
            return render(request, 'search_results_many.html',
                          {'users': users, 'query': q})
        else:
            return HttpResponse('Wrong input')
    else:
        return HttpResponse('Please submit a search term.')


def show_users(request):
    return HttpResponse(DataBase(BASE_NAME).take_users())
