from django.http import HttpResponse
import json
import pickle
import jsonpickle
from .models import Student

def get_student_data():
    students = Student.objects.all()
    student_data = [
        {'name': student.name, 'age': student.age, 'city': student.city}
        for student in students
    ]
    return student_data

def json_view(request):
    student_data = get_student_data()
    serialized_data = json.dumps(student_data, indent=4)
    response = HttpResponse(serialized_data, content_type='application/json')
    return response

def jsonpickle_view(request):
    student_data = get_student_data()
    serialized_data = jsonpickle.encode(student_data, unpicklable=False)
    response = HttpResponse(serialized_data, content_type='application/json')
    return response
