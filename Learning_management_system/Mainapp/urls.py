from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('accounts/', include('allauth.urls')),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
]

