from django.db import models
from django.urls import reverse

# Create your models here.



class Company(models.Model):
	name = models.CharField(max_length=88)
	location = models.CharField(max_length=88)
	ceo = models.CharField(max_length=88)


	def get_absolute_url(self):
		return reverse('detail', kwargs={'pk':self.pk})

'''
ImproperlyConfigured at /create/
No URL to redirect to.  Either provide a url or define a get_absolute_url method on the Model.'''
