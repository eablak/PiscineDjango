from django.db import models

# Create your models here.

class Planets(models.Model):

    name = models.CharField(max_length=64, unique=True, null=False)
    climate = models.CharField()
    diameter = models.IntegerField()
    orbital_period = models.IntegerField()
    population = models.BigIntegerField()
    rotation_period = models.IntegerField()
    surface_water = models.FloatField()
    terrain = models.CharField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    

class People(models.Model):
    
    name = models.CharField(max_length=64, null=False)
    birth_year = models.CharField(max_length=32, null=False)
    gender = models.CharField(max_length=32)
    eye_color = models.CharField(max_length=32)
    hair_color = models.CharField(max_length=32)
    height = models.IntegerField()
    mass = models.FloatField()
    homeworld = models.ForeignKey(Planets, to_field='name', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
