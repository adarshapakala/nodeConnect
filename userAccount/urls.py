from django.urls import path

from . import views

urlpatterns=[
    path('loginOrRegister',views.loginOrRegister , name='loginOrRegister')
    ]