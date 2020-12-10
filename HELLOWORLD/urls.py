from django.contrib import admin
from django.urls import path, re_path
from firstapp import views
from views import Userview, UserActions, MessageViewActions, UserMessenger

urlpatterns = [
    path('', views.index, name='home'),
    path('admin/', admin.site.urls),
    path('users/show', Userview.show_users),
    re_path(r'^search-form/$', Userview.search_form),
    re_path(r'^search/$', Userview.search),
    re_path(r'^init-user/$', UserActions.init_user),
    re_path(r'^inited/$', UserActions.inited_user),
    re_path(r'^delete-init/$', UserActions.init_delete_user),
    re_path(r'^deleted-user/$', UserActions.deleted_user),
    re_path(r'^init_show_messages/$', MessageViewActions.init_show_messages),
    re_path(r'^send_message/$', MessageViewActions.send_message),
    re_path(r'^sent_message/$', MessageViewActions.sent_message),
    re_path(r'^show_messages/$', MessageViewActions.show_messages),
    re_path(r'^login_user/$', UserMessenger.login_user),
    re_path(r'^entering_user/$', UserMessenger.entering_user),
    re_path(r'^show_friends/$', UserMessenger.show_friends),
    re_path(r'^added_friend/$', UserMessenger.add_friend),
    re_path(r'^search_for_friends/$', UserMessenger.search_friends),
]
