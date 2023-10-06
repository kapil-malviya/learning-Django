from django.contrib import admin
from .models import ContactInfo1, Student1, Teacher1, Parent, Child, SubChild

# Register your models here.

''' no need
class ContactInfo1Admin(admin.ModelAdmin):
	list_display = ['id', 'name', 'email', 'address']


class Student1Admin(admin.ModelAdmin):
	list_display = ['id', 'rollno', 'marks']


class Teacher1Admin(admin.ModelAdmin):
	list_display = ['id', 'subject', 'salary']

'''

# django admin panel bydefault considers ContactInfo1 fields in
#  Student1 and Teacher1 table., but only in admin panel not in mysql 
#  or other databases

#   |^ same goes for multi level inheritance model

admin.site.register(ContactInfo1)
admin.site.register(Student1)
admin.site.register(Teacher1)
admin.site.register(Parent)
admin.site.register(Child)
admin.site.register(SubChild)