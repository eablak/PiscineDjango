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

        people_path = os.path.join(settings.BASE_DIR, "ex08/datas/people.csv")
        planets_path = os.path.join(settings.BASE_DIR, "ex08/datas/planets.csv")

        with open(planets_path) as f:
            cursor.copy_expert("COPY ex08_planets (name, climate, diameter, orbital_period, population, rotation_period, surface_water, terrain) FROM STDIN DELIMITER '\t' NULL AS 'NULL';", f)

        with open(people_path) as f:
            cursor.copy_expert("COPY ex08_people (name, birth_year, gender, eye_color, hair_color, height, mass, homeworld) FROM STDIN DELIMITER '\t' NULL AS 'NULL';", f)


        conn.commit()
        conn.close()
        return HttpResponse("OK")
    
    except Exception as e:
        return HttpResponse(e)
