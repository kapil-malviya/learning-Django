from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    print('\n This is View \n')
    return HttpResponse('<h1> Hello Folks </h1>')