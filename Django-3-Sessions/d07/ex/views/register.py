from django.shortcuts import render, redirect
from ..forms import RegisterForm
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout
from django.db import models
from .utils import *

def register(request):
    
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            name = get_auth_username(request)
            return redirect("homepage")
    else:
        form = RegisterForm()
    return render (request, "register.html", {"form":form})


def login_page(request):

    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            name = get_auth_username(request)
            return redirect("homepage")
    else:
        form = AuthenticationForm()

    return render(request, "login.html", {"form":form})


def logout_page(request):

    logout(request)
    return render(request, "base.html")
        