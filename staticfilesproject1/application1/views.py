from django.shortcuts import render
import datetime

# Create your views here.

def datetime_view(request):
    date = datetime.datetime.now()
    hrs = int(date.strftime('%H'))
    if hrs < 12 :
        msg = 'hello folks... good morning'
    elif hrs < 16 :
        msg = 'hello folks.. good afternoon'
    elif hrs < 20 :
        msg = 'hello folks.. good evening'
    else :
        msg = 'good night folks'
    my_dict = {'date':date, 'message':msg }
    return render(request, 'application1/htmlfile.html', my_dict)
