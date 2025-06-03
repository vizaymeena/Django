from django.db import models

# Create your models here.

class MovieList(models.Model):
    moviename=models.CharField(max_length=15)
    moviedescription=models.CharField(max_length=10)
    moviefare=models.IntegerField()

    def __str__(self):
        return self.moviename
