from django.shortcuts import render, HttpResponse


# Create your views here.

def home(request):
    print('\n This is view \n')
    return HttpResponse('<h1> Home Page </h1>')