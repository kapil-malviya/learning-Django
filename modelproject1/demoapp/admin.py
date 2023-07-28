from django.contrib import admin
from demoapp.models import Employee

# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):         # predefined words
    list_display = ['id', 'eno', 'ename', 'eaddr', 'esal']            # list_display also predefined words


admin.site.register(Employee, EmployeeAdmin)     # defining above class here
