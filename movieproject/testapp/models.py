from django.db import models

# Create your models here.

class Movie(models.Model) :
	rdate = models.DateField()
	moviename = models.CharField(max_length=28)
	hero = models.CharField(max_length=28)
	heroine = models.CharField(max_length=28)
	rating = models.IntegerField()