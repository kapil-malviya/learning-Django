from django.db import models

# Create your models here.

# -------------------------------------------------------------------

## Abstract base model inheritance

class ContactInfo(models.Model):
	name = models.CharField(max_length=88)
	email = models.EmailField(max_length=98)
	address = models.CharField(max_length=188)

	class Meta:
		abstract = True                # by this, below 2 tables will be created only & not ContactInfo table

'''
Migrations for 'testapp':
  testapp/migrations/0001_initial.py
    - Create model Student
    - Create model Teacher

''' 


class Student(ContactInfo):
	rollno = models.IntegerField()
	marks = models.IntegerField()


class Teacher(ContactInfo):
	subject = models.CharField(max_length=88)
	salary = models.FloatField()



# ----------------------------------------------------------------------

# Multi table (hierarchical) inheritance
#  django specific


class ContactInfo1(models.Model):
	name = models.CharField(max_length=88)
	email = models.EmailField(max_length=98)
	address = models.CharField(max_length=188)

class Student1(ContactInfo1):
	rollno = models.IntegerField()
	marks = models.IntegerField()


class Teacher1(ContactInfo1):
	subject = models.CharField(max_length=88)
	salary = models.FloatField()

'''
  testapp/migrations/0002_contactinfo1_student1_teacher1.py
    - Create model ContactInfo1
    - Create model Student1
    - Create model Teacher1

'''



# ----------------------------------------------------------------------

# Multi level inheritance

class Parent(models.Model):
	field1 = models.CharField(max_length=88)
	field2 = models.CharField(max_length=88)	


class Child(Parent):
	field3 = models.CharField(max_length=88)
	field4 = models.CharField(max_length=88)


class SubChild(Child):
	field5 = models.CharField(max_length=88)


'''
Migrations for 'testapp':
  testapp/migrations/0003_parent_child_subchild.py
    - Create model Parent
    - Create model Child
    - Create model SubChild
'''