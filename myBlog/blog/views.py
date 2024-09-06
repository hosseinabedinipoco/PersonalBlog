from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth.decorators import login_required
from users.models import User
# Create your views here.

def home(request):
    if not request.user.is_authenticated:
        return redirect(f"{settings.LOGIN_URL}")
    users = User.objects.all()
    return render(request, 'home.html', {'users':users})