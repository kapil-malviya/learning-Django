from django.db import models

# Create your models here.

class FilterModel(models.Model) :
	name = models.CharField(max_length=28)
	subject = models.CharField(max_length=28)
	dept = models.CharField(max_length=28)
	date = models.DateField()


# makemigrations : generate sql code

# migrate : execute that sql code

# see table in db admin interface, register this model with the admin