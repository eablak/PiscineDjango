from django.shortcuts import render
from django.http import HttpResponse
import psycopg2
from django.conf import settings
import os
import sys
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
                CREATE TABLE IF NOT EXISTS ex08_planets(
                    id SERIAL PRIMARY KEY,
                    name VARCHAR(64) UNIQUE NOT NULL,
                    climate VARCHAR,
                    diameter INT,
                    orbital_period INT,
                    population BIGINT,
                    rotation_period INT,
                    surface_water REAL,
                    terrain VARCHAR(128)
                );
            """)    
            
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS ex08_people(
                    id SERIAL PRIMARY KEY,
                    name VARCHAR(64) UNIQUE NOT NULL,
                    birth_year VARCHAR(32),
                    gender VARCHAR(32),
                    eye_color VARCHAR(32),
                    hair_color VARCHAR(32),
                    height INT,
                    mass REAL,
                    homeworld VARCHAR(64),
                    CONSTRAINT fk_people FOREIGN KEY (homeworld) REFERENCES ex08_planets(name)
                    );
            """)    
                
           
        conn.close()
        return HttpResponse("OK")
    except Exception as e:
        return HttpResponse(e)
    


def populate(request):

    try:
        conn = get_connection()
        cursor = conn.cursor()

        results = []

        people_path = os.path.join(settings.BASE_DIR, "ex08/datas/people.csv")
        planets_path = os.path.join(settings.BASE_DIR, "ex08/datas/planets.csv")


        with open(planets_path) as f:
            cursor.copy_from(f, "ex08_planets", sep="\t", null="NULL", columns=("name", "climate", "diameter",
                          "orbital_period", "population",
                          "rotation_period", "surface_water", "terrain"))
            results.append("OK")

        with open(people_path) as f:
            cursor.copy_from(f, "ex08_people", sep="\t", null="NULL", columns=("name", "birth_year", "gender", "eye_color", "hair_color", "height", "mass", "homeworld"))
            results.append("OK")


        conn.commit()
        conn.close()
        return HttpResponse("\n".join(str(result) for result in results))

    
    except Exception as e:
        return HttpResponse(e)
    

def display(request):
    
    try:
        conn = get_connection()
        SELECT_TABLE = """SELECT * FROM ex08_people INNER JOIN ex08_planets ON ex08_people.homeworld = ex08_planets.name ORDER BY ex08_people.name"""

        with conn.cursor() as cursor:
            cursor.execute(SELECT_TABLE)
            peoples = cursor.fetchall()

        conn.close()

        if not peoples:
            return HttpResponse("No data available")
        return render(request, "ex08/display.html", {"peoples":peoples})
    
    except Exception as e:
        return HttpResponse(e)