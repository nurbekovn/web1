"""hello URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
# from django.urls import re_path
from firstapp import views
from django.http.response import Http404

urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('sayHello/', include('HelloWorldApp.urls')),
    path('', views.index),
    path('about/', views.about),
    path('contact/', views.contact),
    path('details/', views.details),
    # re_path(r'^about', views.about),
    # re_path(r'^contact', views.contact),
    # re_path(r'^products/$', views.products),
    # re_path(r'^products/(?P<productId>\d+)/', views.products),
    # re_path(r'^users/(?P<id>\d+)/(?P<name>\D+)/', views.users),
    # path('products/', views.products),
    # path('products/<int:productId>/', views.products),
    # path('users/', views.users),
    # path('details', views.details),
    # path('users/<int:id>/<str:name>/', views.users),

]
