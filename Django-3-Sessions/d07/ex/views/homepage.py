from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.conf import settings
from datetime import datetime, timedelta
import random
from ..models import TipModel
from ..forms import TipModelForm
from .register import get_auth_username
from .utils import *


def homepage(request):

    name = ""
    if request.user.is_authenticated:
        name = get_auth_username(request)
    else:
        name = get_notauth_name(request)
    
    context = {}
    context["tips"] = TipModel.objects.all()
    context["tip_form"] = TipModelForm(request.POST)
    context["name"] = name

    if request.method == "POST":
        form = TipModelForm(data=request.POST)
        if form.is_valid():
            tip = form.save(commit=False)
            tip.author = request.user
            tip.save()
            context["tip_form"] = TipModelForm()
            return render(request, "homepage.html", context)

    return render(request, "homepage.html", context)



def getUserName(request):

    name = get_notauth_name(request)
    return JsonResponse({"name": name})
