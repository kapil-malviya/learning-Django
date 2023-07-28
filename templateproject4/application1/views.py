from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.

def wish(request):
    dt = datetime.datetime.now()
    hrs = int(dt.strftime('%H'))
    msg = 'Hello Folks..! Good '
    if hrs < 12 :
        msg = msg + 'Morning'
    elif hrs < 16 :
        msg = msg + 'AfterNoon'
    elif hrs < 20 :
        msg = msg + 'Evening'
    else :
        msg = msg + 'Night'
    response = render(request, 'application1/one.html',{'message':msg, 'date':dt})
    return response
