from django.db import models

# Create your models here.
from django.db import models

# Create your models here.

class Planets(models.Model):

    name = models.CharField(max_length=64, unique=True, null=False)
    climate = models.CharField(null=True)
    diameter = models.IntegerField(null=True)
    orbital_period = models.IntegerField(null=True)
    population = models.BigIntegerField(null=True)
    rotation_period = models.IntegerField(null=True)
    surface_water = models.FloatField(null=True)
    terrain = models.CharField(null=True)
    created = models.DateTimeField(null=True)
    updated = models.DateTimeField(null=True)

    def __str__(self):
        return self.name
    

class People(models.Model):
    
    name = models.CharField(max_length=64, null=False)
    birth_year = models.CharField(max_length=32, null=True)
    gender = models.CharField(max_length=32, null=True)
    eye_color = models.CharField(max_length=32, null=True)
    hair_color = models.CharField(max_length=32, null=True)
    height = models.IntegerField(null=True)
    mass = models.FloatField(null=True)
    homeworld = models.ForeignKey(Planets, on_delete=models.CASCADE, null=True)
    created = models.DateTimeField(null=True)
    updated = models.DateTimeField(null=True)

    def __str__(self):
        return self.name


class Movies(models.Model):

    title = models.CharField(max_length=64, unique=True, null=False)
    episode_nb = models.IntegerField(primary_key=True)
    opening_crawl = models.TextField()
    director = models.CharField(max_length=32, null=False)
    producer = models.CharField(max_length=128, null=False)
    release_date = models.DateField(null=False)
    characters = models.ManyToManyField(to=People)

    def __str__(self):
        return self.title
