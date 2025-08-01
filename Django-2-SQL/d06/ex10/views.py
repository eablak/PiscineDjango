from django.shortcuts import render
from django.http import HttpResponse
from .forms import InputForm

# Create your views here.

def display(request):
    context = {}
    context["form"] = InputForm()
    return render(request, "ex10/display.html", context)