from django.shortcuts import render
from dbwork import DataBaseUsers, BASE_NAME, DataBaseMessages
from settings import MESSAGE_BASE


class Userview:

    @staticmethod
    def search_form(request):
        return render(request, 'search_form.html')

    @staticmethod
    def show_users(request):
        return render(request, 'search_results_many.html',
                      {'users': DataBaseUsers(BASE_NAME).take_users(), 'query': ''})

    @staticmethod
    def search(request):
        q = request.GET['q']
        types = request.GET['type']
        types = types.strip()
        if types == '' or types == 'ALL':
            users = DataBaseUsers(BASE_NAME).take_users()
        else:
            users = DataBaseUsers(BASE_NAME).take_users(types, q)
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
        DataBaseUsers(BASE_NAME).init_data_base()
        return render(request, 'inited_user.html',
                      {'user': DataBaseUsers(BASE_NAME).init_user(request.POST['Name'], int(request.POST['Age']))
                       }
                      )

    @staticmethod
    def init_delete_user(request):
        return render(request, 'delete_init.html')

    @staticmethod
    def deleted_user(request):
        user = DataBaseUsers(BASE_NAME).del_user(int(request.POST['ids']), request.POST['Name'])
        if user.id != -1:
            return render(request, 'deleted_user.html', {'user': user, 'type': True})
        else:
            return render(request, 'deleted_user.html', {'user': user, 'type': False})


class MessageViewActions:

    @staticmethod
    def init_show_messages(request):
        return render(request, 'init_show_messages.html')

    @staticmethod
    def show_messages(request):
        table = DataBaseMessages(MESSAGE_BASE).show_messages(request.GET['idhost'], request.GET['idfriend'])
        return render(request, 'show_messages.html', {'idhost': request.GET['idhost'],
                                                      'hostname': DataBaseUsers(BASE_NAME).take_user_name(
                                                          request.GET['idhost']),
                                                      'idfriend': request.GET['idfriend'], 'table': table,
                                                      'friendname': DataBaseUsers(BASE_NAME).take_user_name(
                                                          request.GET['idfriend'])})

    @staticmethod
    def send_message(request):
        return render(request, 'send_message.html')

    @staticmethod
    def sent_message(request):
        DataBaseMessages(MESSAGE_BASE).send_message(request.POST['idhost'], request.POST['idfriend'],
                                                    request.POST['message'])
        return render(request, 'sent_message.html')


def index(request):
    return render(request, "index.html")
