from django.contrib import admin
from django.urls import include,path
from phonebook import views

urlpatterns = [
    path('',views.index, name='index'),
    path('addContact/',views.addContact, name = 'addContact')
]
