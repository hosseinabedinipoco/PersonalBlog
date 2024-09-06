from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth.decorators import login_required
from users.models import User
# Create your views here.

def home(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect(f"{settings.LOGIN_URL}")
    user = User.objects.get(pk=user_id)
    return render(request, 'home.html', {'user':user})

def index(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect(f"{settings.LOGIN_URL}")
    user = User.objects.get(pk=user_id)
    if not user.is_Admin:
        return redirect(f"{settings.LOGIN_URL}")
    return render(request, 'index.html', {'user':user})