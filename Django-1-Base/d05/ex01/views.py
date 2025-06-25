from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def django(request):
    return HttpResponse("django page")

def display(request):
    return HttpResponse("display page")

def templates(request):
    return HttpResponse("templates page")