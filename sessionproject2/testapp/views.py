from django.shortcuts import render
from testapp.forms import NameForm, AgeForm, GFForm

# Create your views here.


def name_view(request) :
	form = NameForm()
	return render(request, 'testapp/name.html', {'form':form})


def age_view(request):
	name = request.GET['name']
	request.session['name'] = name
	form = AgeForm()
	return render(request, 'testapp/age.html', {'form':form})


def gf_view(request):
	age = request.GET['age']
	request.session['age'] = age
	form = GFForm()
	return render(request, 'testapp/gf.html', {'form':form})


def result_view(request):
	gf = request.GET['gf']
	request.session['gf'] = gf
	return render(request, 'testapp/result.html')