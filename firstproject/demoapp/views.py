from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def myview(request):
    return HttpResponse('<h1> hello this is response from django application </h1>')
