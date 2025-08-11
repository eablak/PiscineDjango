from django.shortcuts import render
import os
from django.conf import settings
import json
from .models import Movies
from django.db import IntegrityError
from django.http import HttpResponse
from .forms import InputForm
# Create your views here.


def populate(request):
    path = os.path.join(settings.BASE_DIR , "ex02/data/datas.json")
    with open(path) as f:
        movies = json.load(f)

    results = []

    for movie in movies:
        try:
            Movies.objects.create(
                episode_nb=movie['episode_nb'],
                title = movie["title"],
                director=movie['director'],
                producer=movie['producer'],
                release_date=movie['release_date'],
            )
            results.append("OK")
        except IntegrityError:
            pass
        except Exception as e:
            return HttpResponse(f"Error {e}")
    return HttpResponse("\n".join(str(result) for result in results))



def display(request):
    try:
        movies = Movies.objects.all()
        if not movies:
            return HttpResponse("No data available")
        return render(request, "ex07/display.html", {"movies":movies})
    except Exception as e:
        return HttpResponse(e)
    


def update(request):
    

    context = {}

    if request.method == "GET":

        try:
            titles = Movies.objects.values_list("title")
            
            if not titles:
                return HttpResponse("No data available")
            
            context["titles"] = titles
            context["form"] = InputForm()
            return render(request, "ex07/update.html", context)
        except Exception as e:
            return HttpResponse(e)
    
    if request.method == "POST":
        
        text = ""
        form = InputForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data["textfield"]
        title = request.POST.get("selected_movie")

        Movies.objects.filter(title=title).update(opening_crawl=text)

        titles = Movies.objects.values_list("title")
            
        if not titles:
            return HttpResponse("No data available")
        
        context["titles"] = titles
        context["form"] = InputForm()

        return render(request, "ex07/update.html", context)
        
