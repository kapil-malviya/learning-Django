from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def good_morning_view(request):
    return HttpResponse('<h1> Hello Kapil good morning !!! </h1>')


def good_afternoon_view(request):
    return HttpResponse('<h3> Hello Kapil good afternoon !!! </h3>')


def good_evening_view(request):
    return HttpResponse('<h3> Hello Kapil good evening !!! </h3>')


def good_night_view(request):
    return HttpResponse('<h1> Hello Kapil good night !!! </h1>')
