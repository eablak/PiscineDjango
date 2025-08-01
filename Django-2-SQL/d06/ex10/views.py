from django.shortcuts import render
from django.http import HttpResponse
from .forms import InputForm
from .models import *

# Create your views here.

def display(request):

    if request.method == "GET":
        context = {}
        context["form"] = InputForm()
        return render(request, "ex10/display.html", context)
    

    if request.method == "POST":

        form = InputForm(request.POST)

        if form.is_valid():
            min_date = form.cleaned_data["minimumDate_movies"]
            max_date = form.cleaned_data["maximumDate_movies"]
            min_diameter = form.cleaned_data["diameter_planet"]
            gender = form.cleaned_data["Gender Character"]

            match_characters = People.objects.filter(movies__release_date__range=(min_date,max_date)).filter(homeworld__diameter__gte=min_diameter).filter(gender=gender).distinct()


            results = []
            # give related_name to many to many column and use it instead of movies_set
            for character in match_characters:
                movie_range = character.movies_set.filter(release_date__range=(min_date,max_date))
                for movie in movie_range:
                    if character.homeworld.diameter >= min_diameter:
                        results.append({
                            "movie_title": movie.title,
                            "character_name": character.name,
                            "gender": character.gender,
                            "homeworld_name": character.homeworld.name,
                            "diameter": character.homeworld.diameter
                        })
            context = {}
            context["results"] = results
            return render(request, "ex10/results.html", context)
        else:
            form = InputForm()

    else:
        context = {}
        context["form"] = InputForm()
        return render(request, "ex10/display.html", context)