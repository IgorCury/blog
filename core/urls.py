from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contato', views.contato, name="contato"),
    path('projeto', views.projeto, name="projeto"),
    path('sobre', views.sobre, name="sobre")
]