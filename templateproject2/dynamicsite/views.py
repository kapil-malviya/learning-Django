from django.shortcuts import render
import datetime

# Create your views here.

def temp_view(request):
    dt = datetime.datetime.now()
    my_dict = {'date':dt}
    return render(request, 'dynamicsite/time.html', my_dict)
#    return render(request, 'dynamicsite/time.html', {'date':dt})
