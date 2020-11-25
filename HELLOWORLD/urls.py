from django.contrib import admin
from django.urls import path, re_path
from firstapp import views
from views import Userview, Userclass

urlpatterns = [
    path('', views.index, name='home'),
    path('admin/', admin.site.urls),
    path('users/show', Userview.show_users),
    re_path(r'^search-form/$', Userview.search_form),
    re_path(r'^search/$', Userview.search),
    re_path(r'^init-user/$', Userclass.init_user),
    re_path(r'^inited/$', Userclass.inited_user),
    re_path(r'^delete-init/$', Userclass.init_delete_user),
    re_path(r'^deleted-user/$', Userclass.deleted_user),
]
