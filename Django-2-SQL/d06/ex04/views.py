from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
# Create your views here.
import psycopg2
import os
import json


def get_connection():
    return psycopg2.connect(
        dbname = settings.DATABASES["default"]["NAME"],
        user = settings.DATABASES["default"]["USER"],
        password = settings.DATABASES["default"]["PASSWORD"],
        host = settings.DATABASES["default"]["HOST"],
        port = settings.DATABASES["default"]["PORT"]
    )

def init(request):
    
    try:
        conn = get_connection()
        conn.autocommit = True
        with conn.cursor() as cursor:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS ex04_movies(
                    title VARCHAR(64) UNIQUE NOT NULL,
                    episode_nb INT PRIMARY KEY,
                    opening_crawl TEXT,
                    director VARCHAR(32) NOT NULL,
                    producer VARCHAR(128) NOT NULL,
                    release_date DATE NOT NULL);
            """)
            conn.close()
            return HttpResponse("OK")
    except Exception as e:
        return HttpResponse(e)
    
def populate(request):
    
    try:
        conn = get_connection()
        
        path = os.path.join(settings.BASE_DIR, "ex02/data/datas.json")
        with open(path) as f:
            movies = json.load(f)

        INSERT_DATA = """
            INSERT INTO ex04_movies(episode_nb, title, director, producer, release_date)
            VALUES (%s, %s, %s, %s, %s) ON CONFLICT (episode_nb) DO NOTHING;
        """

        results = []

        with conn.cursor() as cursor:
            for movie in movies:
                cursor.execute(INSERT_DATA, [
                    movie["episode_nb"],
                    movie["title"],
                    movie["director"],
                    movie["producer"],
                    movie["release_date"]
                ])
                results.append("OK")
            conn.commit()
        return HttpResponse("\n".join(str(result) for result in results))
    except Exception as e:
        return HttpResponse(e)


def display(request):
    
    try:
        conn = get_connection()

        SELECT_TABLE = """SELECT * FROM ex04_movies"""

        with conn.cursor() as cursor:
            cursor.execute(SELECT_TABLE)
            movies = cursor.fetchall()
        
        conn.close()

        if not movies:
            return HttpResponse("No data available")
        return render(request, "ex04/display.html", {"movies":movies})

    except Exception as e:
        return HttpResponse(e)
    

def remove(request):

    if request.method == "GET":

        try:
            conn = get_connection()

            SELECT_TITLE = """SELECT title FROM ex04_movies"""

            with conn.cursor() as cursor:
                cursor.execute(SELECT_TITLE)
                movies = cursor.fetchall()
            conn.close()

            if not movies:
                return HttpResponse("No data available")
            return render(request, "ex04/remove.html", {"movies":movies})
        except Exception as e:
            return HttpResponse(e)
        
    if request.method == "POST":

        try:
            conn  = get_connection()
            title = request.POST.get("title")
            DELETE_ROW = """DELETE FROM ex04_movies WHERE title=%s"""
            SELECT_TITLE = """SELECT title FROM ex04_movies"""
            
            with conn.cursor() as cursor:
                cursor.execute(DELETE_ROW, (title,))
                cursor.execute(SELECT_TITLE)
                movies = cursor.fetchall()
            conn.commit()
            conn.close()

            if not movies:
                return HttpResponse("No data available")
            return render(request, "ex04/remove.html", {"movies":movies})

        except Exception as e:
            return HttpResponse(e)