from django.shortcuts import render
from django.http import HttpResponse
import psycopg2
from django.conf import settings
import os
import json
from .forms import InputForm
# Create your views here.


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
            CREATE TABLE IF NOT EXISTS ex06_movies(
                title VARCHAR(64) UNIQUE NOT NULL,
                episode_nb INT PRIMARY KEY,
                opening_crawl TEXT,
                director VARCHAR(32) NOT NULL,
                producer VARCHAR(128) NOT NULL,
                release_date DATE NOT NULL,
                created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                );
            """)

            cursor.execute("""
                CREATE OR REPLACE FUNCTION update_changetimestamp_column()
                RETURNS TRIGGER AS $$
                BEGIN
                NEW.updated = now();
                NEW.created = OLD.created;
                RETURN NEW;
                END;
                $$ language 'plpgsql';
            """)

            cursor.execute("""CREATE TRIGGER update_films_changetimestamp BEFORE UPDATE
                ON ex06_movies FOR EACH ROW EXECUTE PROCEDURE
                update_changetimestamp_column();
            """)

        conn.close()
        return HttpResponse("OK")
    except Exception as e:
        return HttpResponse(e)
    

def populate(request):

    try:
        conn = get_connection()
        
        path = os.path.join(settings.BASE_DIR , "ex02/data/datas.json")
        with open(path) as f:
            movies = json.load(f)

        INSERT_DATA = """
            INSERT INTO ex06_movies (episode_nb, title, director, producer, release_date)
            VALUES (%s, %s, %s, %s, %s);
        """

        results = []

        with conn.cursor() as cursor:
            for movie in movies:
                cursor.execute(INSERT_DATA, [
                    movie["episode_nb"],
                    movie["title"],
                    movie["director"],
                    movie["producer"],
                    movie["release_date"],
                ])
                results.append("OK")
            conn.commit()
            conn.close()
        return HttpResponse("\n".join(str(result) for result in results))
    
    except Exception as e:
        return HttpResponse(e)
    
def display(request):

    try:
        conn = get_connection()

        SELECT_TABLE = """
        SELECT * FROM ex06_movies
    """

        with conn.cursor() as cursor:
            cursor.execute(SELECT_TABLE)
            movies = cursor.fetchall()
        conn.close()

        if not movies:
            return HttpResponse("No data available")
        return render(request, "ex06/display.html", {"movies":movies})

    except Exception as e:
        return HttpResponse(e)
    
def update(request):

    if request.method == "GET":

        try:
            conn = get_connection()

            SELECT_TITLE = """SELECT title FROM ex06_movies"""

            with conn.cursor() as cursor:
                cursor.execute(SELECT_TITLE)
                movies = cursor.fetchall()
            conn.close()

            if not movies:
                return HttpResponse("No data available")
            
            context = {
                "movies": movies,
                "form": InputForm() 
            }
            return render(request, "ex06/update.html",context)
        except Exception as e:
            return HttpResponse(e)
    
    
    if request.method == "POST":

        context = {}
        context["form"] = InputForm()

        try:
            conn  = get_connection()
            
            form = InputForm(request.POST)
            text = ""
            if form.is_valid():
                text = form.cleaned_data["textfield"]
            title = request.POST.get("selected_movie")

            UPDATE = """UPDATE ex06_movies SET opening_crawl =%s where title=%s"""
            SELECT_TITLE = """SELECT title FROM ex06_movies"""

            with conn.cursor() as cursor:
                cursor.execute(UPDATE, (text,title))
                cursor.execute(SELECT_TITLE)
                movies = cursor.fetchall()
                context["movies"] = movies

            conn.commit()
            conn.close()

            if not movies:
                return HttpResponse("No data available")
            return render(request, "ex06/update.html", context)
        
        except Exception as e:
            return HttpResponse(e)