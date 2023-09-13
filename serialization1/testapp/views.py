from django.shortcuts import render
from .models import Student
import json
from django.http import HttpResponse

# Create your views here.

def students(request):
	students = Student.objects.all()
	student_data = [{'name':student.name, 'age':student.age, 'city':student.city} for student in students]

	serialized_data = json.dumps(student_data, indent=4)

	return HttpResponse(serialized_data)