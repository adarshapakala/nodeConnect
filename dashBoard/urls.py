from django.urls import path

from . import views

urlpatterns=[
    path('welcomeDashboard',views.welcomeDashboard , name='welcomeDashboard'),
    ]