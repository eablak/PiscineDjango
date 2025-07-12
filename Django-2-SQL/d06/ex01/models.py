from django.db import models

# Create your models here.
class Movies(models.Model):

    title = models.CharField(max_length=64, unique=True, null=False)
    episode_nb = models.IntegerField(primary_key=True)
    opening_crawl = models.TextField()
    director = models.CharField(max_length=32, null=False)
    producer = models.CharField(max_length=128, null=False)
    release_date = models.DateField(null=False)

    # automaticlly -> appname_modelname
    # class Meta:
    #     db_table = "ex01_movies"

    def __str__(self):
        return self.title