from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .forms import *
from .models import User
from django.contrib.auth import login as django_login
from django.conf import settings
from django.contrib.sessions.backends.db import SessionStore


def login(request):
    if request.method == 'GET':
        form = LoginForm()
        return render(request, 'login.html', {'form':form})
    elif request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form['username'].value()
            password = form['password'].value()
            custom_error = {}
            try:
                user = User.objects.get(username=username)
                if user.password != password:
                    custom_error['password'] = 'incorrect password'
                    form._errors.update(custom_error)
                else:       
                    request.session["user_id"] = user.id
                    return redirect('home')
            except User.DoesNotExist:
                custom_error['username'] = 'there is not this username'
                form._errors.update(custom_error)
    return render(request, 'login.html', {'form':form})


