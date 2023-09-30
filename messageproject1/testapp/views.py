from django.shortcuts import render
from .forms import StudentRegistration
from django.contrib import messages

# Create your views here.

def registration(request):
	if request.method == 'POST':
		form = StudentRegistration(request.POST)
		if form.is_valid():
			form.save()
			messages.add_message(request, messages.SUCCESS, 'Your account has been created')
			messages.info(request, 'Now you can login...')
	else :
		form = StudentRegistration()
	return render(request, 'testapp/registration.html', {'form':form})