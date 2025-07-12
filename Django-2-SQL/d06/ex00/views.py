from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
import psycopg2
from django.conf import settings
# Create your views here.

def index(request):
    # return HttpResponse("initctt")

    try:
        conn = psycopg2.connect(
            dbname = settings.DATABASES["default"]["NAME"],
            user = settings.DATABASES["default"]["USER"],
            password = settings.DATABASES["default"]["PASSWORD"],
            host = settings.DATABASES["default"]["HOST"],
            port = settings.DATABASES["default"]["PORT"]
        )
        conn.autocommit = True
        with conn.cursor() as cursor:
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS ex00_movies(
                title VARCHAR(64) UNIQUE NOT NULL,
                episode_nb INT PRIMARY KEY,
                opening_crawl TEXT,
                director VARCHAR(32) NOT NULL,
                producer VARCHAR(128) NOT NULL,
                release_date DATE NOT NULL
                );
            """)
            conn.close()
            return HttpResponse("OK")
    except Exception as e:
        return HttpResponse(e)