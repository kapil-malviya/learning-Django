from django.shortcuts import render
import datetime
from django.http import HttpResponse

# Create your views here.
def date_time_view(request):
    date = datetime.datetime.now()
    response = '<h2> The current date & time is : ' + str(date) + '</h2>'
    return HttpResponse(response)
