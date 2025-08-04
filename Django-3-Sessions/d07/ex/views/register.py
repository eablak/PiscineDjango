from django.shortcuts import render, redirect
from ..forms import RegisterForm
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

def register(request):
    
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("")
    else:
        form = RegisterForm()

    return render (request, "register.html", {"form":form})


def login_page(request):

    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect("homepage")
    else:
        form = AuthenticationForm()

    return render(request, "login.html", {"form":form})
        