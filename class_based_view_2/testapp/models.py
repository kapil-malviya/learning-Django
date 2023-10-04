from django.db import models

# Create your models here.


class Book(models.Model):
	title = models.CharField(max_length=88)
	author = models.CharField(max_length=88)
	pages = models.PositiveIntegerField()
	price = models.FloatField()