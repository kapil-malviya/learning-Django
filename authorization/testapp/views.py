from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm
from django.http import HttpResponseRedirect

# Create your views here.

def home_page_view(request) :
	return render(request, 'testapp/home.html')

@login_required
def java_exam_view(request) :
	return render(request, 'testapp/javaexams.html')

@login_required
def python_exam_view(request) :
	return render(request, 'testapp/pythonexams.html')

@login_required
def aptitude_exam_view(request) :
	return render(request, 'testapp/aptitudeexams.html')

def logout_view(request) :
	return render(request, 'testapp/logout.html')


def signup_view(request) :
	form = SignUpForm()
	if request.method=='POST' :
		form = SignUpForm(request.POST)
#		if form.is_valid() :               # it is also valid, it is encrypting the password
#			form.save()          
	#	form.save()                        # it won't save passwords in hash form, so user won't be able to login
		user = form.save()
		user.set_password(user.password)   # password saved in encrypted form
		user.save()
		return HttpResponseRedirect('/accounts/login')
	return render(request, 'testapp/signup.html', {'form':form})