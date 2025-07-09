from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.conf import settings
from .forms import InputForm
import logging


def index(request):

    logger = logging.getLogger('history_log')
    context = {}
    context["form"] = InputForm()

    if request.method == "POST":
        form = InputForm(request.POST)
        if form.is_valid():
            logger.info(form.cleaned_data["textfield"])
            return redirect("/ex02")
    
    file = open(settings.LOG_FILE, "r")
    context["lines"] = [line.strip() for line in file]

    return render(request, "ex02/index.html", context)