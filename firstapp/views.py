from django.shortcuts import render
from dbwork import DataBase, BASE_NAME


class Userview:

    @staticmethod
    def search_form(request):
        return render(request, 'search_form.html')

    @staticmethod
    def show_users(request):
        return render(request, 'search_results_many.html',
                      {'users': DataBase(BASE_NAME).take_users(), 'query': ''})

    @staticmethod
    def search(request):
        q = request.GET['q']
        types = request.GET['type']
        types = types.strip()
        if types == '' or types == 'ALL':
            users = DataBase(BASE_NAME).take_users()
        else:
            users = DataBase(BASE_NAME).take_users(types, q)
        if types == 'ONE':
            q = list(q.split(';'))[0]
        return render(request, 'search_results_many.html',
                      {'users': users, 'query': q})


class UserActions:

    @staticmethod
    def init_user(request):
        return render(request, 'init_user.html')

    @staticmethod
    def inited_user(request):
        DataBase(BASE_NAME).init_data_base()
        return render(request, 'inited_user.html',
                      {'user': DataBase(BASE_NAME).init_user(request.POST['Name'], int(request.POST['Age']))
                       }
                      )

    @staticmethod
    def init_delete_user(request):
        return render(request, 'delete_init.html')

    @staticmethod
    def deleted_user(request):
        user = DataBase(BASE_NAME).del_user(int(request.POST['ids']), request.POST['Name'])
        if user.id != -1:
            return render(request, 'deleted_user.html', {'user': user, 'type': True})
        else:
            return render(request, 'deleted_user.html', {'user': user, 'type': False})


def index(request):
    return render(request, "index.html")
