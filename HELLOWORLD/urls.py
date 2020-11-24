"""HELLOWORLD URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from firstapp import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('admin/', admin.site.urls),
    re_path(r'^products/(?P<productid>\d+)/', views.product),
    re_path(r'^users/init/(?P<ids>\d+)/(?P<name>\D+)/(?P<age>\d+)', views.init_users),
    path('users/show', views.show_users),
    re_path(r'^search-form/$', views.search_form),
    re_path(r'^search/$', views.search),
]
