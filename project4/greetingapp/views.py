from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def greetings_view(request):
    return HttpResponse('<h2> Jai Ganeshh Folks </h2>')
