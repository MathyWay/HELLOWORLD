from django.contrib import admin
from django.urls import path, re_path
from firstapp import views
from views import Userview, UserActions

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
]
