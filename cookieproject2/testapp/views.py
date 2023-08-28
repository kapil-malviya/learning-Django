from django.shortcuts import render

# Create your views here.


def name_view(request) :
	return render(request, 'testapp/name.html')


def age_view(request) :
	name = request.GET['name']    # reading data from name.html
	response = render(request, 'testapp/age.html')
	response.set_cookie('name', name)
	return response


def gf_view(request) :
	age = request.GET['age']
	response = render(request, 'testapp/gf.html')
	response.set_cookie('age', age)
	return response


def result_view(request) :
	gfname = request.GET['gfname']
	name = request.COOKIES.get('name')
	age = request.COOKIES.get('age')
	response = render(request, 'testapp/result.html', {'name':name, 'age':age, 'gfname':gfname})
	response.set_cookie('gfname', gfname)
	return response