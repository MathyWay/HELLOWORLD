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


def init_users1(request):
    return render(request, 'init_user.html')


def inited_user(request):
    DataBase(BASE_NAME).init_data_base()
    DataBase(BASE_NAME).init_user(UserCl(int(request.POST['id']), request.POST['Name'], int(request.POST['Age'])))
    return HttpResponse("User: " + request.POST['Name'] +
                        " with id {0} and Age: {1} added</h2>".format(int(request.POST['id']),
                                                                      int(request.POST['Age'])))


def search_form(request):
    return render(request, 'search_form.html')


def search(request):
    q = request.GET['q']
    types = request.GET['type']
    types = types.strip()
    if types == '' or types == 'ALL':
        users = DataBase(BASE_NAME).take_users()
    else:
        users = DataBase(BASE_NAME).take_users(types, q)
    if type(users) == UserCl:
        return render(request, 'search_results.html',
                      {'users': users, 'query': q})
    elif type(users) == list:
        return render(request, 'search_results_many.html',
                      {'users': users, 'query': q})
    elif users == -1:
        return HttpResponse('There is now such user')
    else:
        return HttpResponse('Wrong input')


def show_users(request):
    return HttpResponse(DataBase(BASE_NAME).take_users())
