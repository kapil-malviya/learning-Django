from django.shortcuts import render, HttpResponse

# Create your views here.

def division(request):
    a = 10/0
    return HttpResponse('hello')