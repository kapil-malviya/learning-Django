from django.contrib import admin
from .models import FilterModel

# Register your models here.

class FilterModelAdmin(admin.ModelAdmin) :
	list_display = ['name', 'subject', 'dept', 'date']




admin.site.register(FilterModel, FilterModelAdmin)