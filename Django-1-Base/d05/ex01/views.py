from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def django(request):
    return render(request, "django.html")

def display(request):
    return render(request, "display.html")

def templates(request):
    return render(request, "templates.html")