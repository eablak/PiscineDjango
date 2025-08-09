from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.conf import settings
from datetime import datetime, timedelta
import random
from ..models import TipModel
from ..forms import TipModelForm
from .register import get_auth_username
from .utils import *
from django.contrib.auth.models import User


def upvote_tip(request, tip_id):

    tip = TipModel.objects.get(id=tip_id)
    users = tip.upvoter.all()

    if request.user in users:
        tip.upvoter.remove(request.user)
    else:
        if request.user in tip.downvoter.all():
            tip.downvoter.remove(request.user)
        tip.upvoter.add(request.user)

    return redirect ("homepage")


def downvote_tip(request, tip_id):
    
    tip = TipModel.objects.get(id=tip_id)
    users = tip.downvoter.all()

    if request.user in users:
        tip.downvoter.remove(request.user)
    else:
        if request.user in tip.upvoter.all():
            tip.upvoter.remove(request.user)
        tip.downvoter.add(request.user)
        
        if tip.downvoter.count() >= User.objects.count() * 0.7: 
            tip.delete()
    return redirect("homepage")


def delete_tip(request, tip_id):
    
    tip = TipModel.objects.get(id=tip_id)
    tip.delete()
    return redirect("homepage")

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
