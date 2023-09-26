from django.db import models

# Create your models here.


class Employee(models.Model):
	eno = models.IntegerField()
	ename = models.CharField(max_length=88)
	esal = models.IntegerField()
	ecity = models.CharField(max_length=88)
	