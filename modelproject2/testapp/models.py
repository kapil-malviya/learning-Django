from django.db import models

# Create your models here.

class Student(models.Model):
	stuid = models.IntegerField()
	stuname = models.CharField(max_length=48)
	stumail = models.EmailField(max_length=48)
	stupass = models.CharField(max_length=48)

	def __str__(self):
		return self.stumail, self.stuname