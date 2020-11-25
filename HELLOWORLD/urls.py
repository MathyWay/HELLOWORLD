from django.contrib import admin
from django.urls import path, re_path
from firstapp import views
from views import Userview, InitUser

urlpatterns = [
    path('', views.index, name='home'),
    path('admin/', admin.site.urls),
    path('users/show', Userview.show_users),
    re_path(r'^search-form/$', Userview.search_form),
    re_path(r'^search/$', Userview.search),
    re_path(r'^init-user/$', InitUser.init_user),
    re_path(r'^inited/$', InitUser.inited_user),
]
