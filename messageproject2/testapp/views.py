from django.shortcuts import render
from .forms import StudentRegistration
from django.contrib import messages

# Create your views here.

def registration(request):
	if request.method == 'POST':
		form = StudentRegistration(request.POST)
		if form.is_valid():
			form.save()
			messages.info(request, 'Now you can login...')
			print("get_level(request) : ", messages.get_level(request))
			
			messages.warning(request, 'this is warning')
			messages.set_level(request, messages.WARNING)
			messages.warning(request, 'this is NEW warning')
			print("get_level(request) : ", messages.get_level(request))

			messages.debug(request, 'This is debug')
			messages.set_level(request, messages.DEBUG)
			messages.debug(request, 'This is NEW debug')
			print("get_level(request) : ", messages.get_level(request))
	else :
		form = StudentRegistration()
	return render(request, 'testapp/registration.html', {'form':form})