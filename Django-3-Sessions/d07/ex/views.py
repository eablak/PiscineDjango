from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
import random
# Create your views here.

def init(request):
   
    request.session["name"] = random.choice(settings.NAMES)
    context = {}
    context["name"] = request.session["name"]
    return render(request, "ex00.html", context)