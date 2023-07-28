from django.shortcuts import render
from demoapp.models import Employee

# Create your views here.

def employee_info_view(request):
    employees = Employee.objects.all()          # internally => queryset
    return render(request, 'demoapp/result.html', {'employees':employees})
