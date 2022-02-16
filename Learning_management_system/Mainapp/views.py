from django.http.response import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User, auth
from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'Mainapp/index.html')

def login(request):
    if request.method == 'POST':
        user_name = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=user_name, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'User Does not Exist')
            return redirect('/login/')
    return render(request, 'account/login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')