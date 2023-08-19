from django.shortcuts import render
from . import forms

# Create your views here.

def student_view(request) :
	form = forms.StudentForm()
	context = {'form' : form}
	if request.method=='POST' :
		form = forms.StudentForm(request.POST)
		if form.is_valid() :
			form.save()
			print('Form data insterted successfully')
	return render(request, 'testapp/register.html', context)