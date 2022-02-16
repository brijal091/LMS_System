from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required   # This is used to restrict access to a view to logged in users only.

# Create your views here.
@login_required
def admin_home(request):
    if request.user.is_superuser:
        return render(request, 'admin_dashboard/admin_home.html')
    else:
        return render(request, '../Main_app/index.html')