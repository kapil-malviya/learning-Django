from django.shortcuts import render
import datetime

# Create your views here.

def my_view(request):
    dt = datetime.datetime.now()
    my_dict = {'date':dt, 'name':'Kapil', 'worth':'Bahut', 'age':'Amar hai'}
    return render(request, 'dicttemplate/dict.html', my_dict)
