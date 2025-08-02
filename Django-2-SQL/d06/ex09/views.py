from django.shortcuts import render
from .models import Planets, People
from django.http import HttpResponse

# Create your views here.

def display(request):

    try:
        peoples = People.objects.all().order_by("name")
        context = {"peoples":peoples}
        
        if not peoples:
            return HttpResponse("No data available, please use the following command line before use: python3 manage.py loaddata ex09/ex09_initial_data.json")
        return render(request, "ex09/display.html", context)
    except Exception as e:
        return HttpResponse(e)