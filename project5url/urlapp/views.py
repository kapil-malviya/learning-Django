from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def first_view(request):
    return HttpResponse('<h1> Response from the first view </h1>')


def second_view(request):
    return HttpResponse('<h1> Response from the second view </h1>')


def third_view(request):
    return HttpResponse('<h1> Response from the third view </h1>')


def fourth_view(request):
    return HttpResponse('<h1> Response from the fourth view </h1>')


def fifth_view(request):
    return HttpResponse('<h1> Response from the fifth view </h1>')
