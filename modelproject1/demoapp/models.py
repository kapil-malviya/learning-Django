from django.db import models

# Create your models here.

class Employee(models.Model):
    eno = models.IntegerField()
    ename = models.CharField(max_length=68)
    esal = models.FloatField()
    eaddr = models.CharField(max_length=68)


    def __str__(self):
        return self.ename        # to display Employee name on the db table on admin console
