from django.shortcuts import render
from django.http import HttpResponse
import os
from django.conf import settings
import json
from .models import Movies
from django import db
from django.db import IntegrityError


# Create your views here.
def populate(request):
    path = os.path.join(settings.BASE_DIR , "ex03/data/datas.json")
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
            results.append(e)
    return HttpResponse("\n".join(str(result) for result in results))


def display(request):
    
    try:
        movies = Movies.objects.all()
        if not movies:
            return HttpResponse("No data available")
        return render(request, "ex03/display.html", {"movies":movies})
    except Exception as e:
        return HttpResponse(e)