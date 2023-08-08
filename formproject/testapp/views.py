from django.shortcuts import render
from . import forms

# Create your views here.

def studentregisterview(request) :
	form = forms.StudentRegistration()
	return render(request, 'testapp/register.html', {'form':form})