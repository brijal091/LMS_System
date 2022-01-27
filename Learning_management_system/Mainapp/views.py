from django.http.response import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User, auth
from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return render(request, 'Mainapp/index.html')
