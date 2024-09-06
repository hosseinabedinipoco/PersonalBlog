from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .forms import *
from .models import User
from django.contrib.auth import login as django_login
from django.conf import settings
from django.contrib.sessions.backends.db import SessionStore
from django.contrib.auth.hashers import make_password


def login(request):
    if request.method == 'GET':
        form = LoginForm()
    elif request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form['username'].value()
            password = form['password'].value()
            custom_error = {}
            try:
                user = User.objects.get(username=username)
                if user.check_password(password):
                    custom_error['password'] = 'incorrect password'
                    form._errors.update(custom_error)
                else:       
                    request.session["user_id"] = user.id
                    if user.is_Admin:
                        return redirect('index')
                    return redirect('home')
            except User.DoesNotExist:
                custom_error['username'] = 'there is not this username'
                form._errors.update(custom_error)
    return render(request, 'login.html', {'form':form})

def logout(request):
    request.session.flush()
    return redirect('login')

def register(request):
    if request.method == 'GET':
        form = RegisterForm()
    else:
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form['username'].value()
            password1 = form['password1'].value()
            password2 = form['password2'].value()
            custom_error = {}
            try:
                user = User.objects.get(username=username)
                custom_error['username'] = 'this username already exist'
                form._errors.update(custom_error)
            except User.DoesNotExist:
                if password1 != password2:
                    custom_error['password2'] = 'these must be same'
                    form._errors.update(custom_error)
                else :
                    user = User(username=username, is_Admin=False)
                    user.set_password(password1)
                    user.save()
                    request.session["user_id"] = user.id
                    return redirect('home')
    return render(request, 'register.html', {'form':form})

            
            

