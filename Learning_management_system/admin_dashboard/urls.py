from . import views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', views.admin_home, name='admin_home'),
]