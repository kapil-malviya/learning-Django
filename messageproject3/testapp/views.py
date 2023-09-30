from django.shortcuts import render
from .forms import StudentRegistration
from django.contrib import messages

# Create your views here.

def registration(request):
	messages.info(request, 'Now you can login..!')
	messages.success(request, 'Form uploaded successfully')
	messages.warning(request, 'warning')
	messages.error(request, 'this is an error')
	if request.method == 'POST':
		form = StudentRegistration(request.POST)
		if form.is_valid():
			form.save()
	else :
		form = StudentRegistration()
	return render(request, 'testapp/registration.html', {'form':form})