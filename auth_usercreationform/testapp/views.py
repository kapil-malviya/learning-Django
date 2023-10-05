from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.


def signup(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
	else :
		form = UserCreationForm()
	return render(request, 'testapp/signup.html', {'form':form})