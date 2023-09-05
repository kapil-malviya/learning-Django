from django.shortcuts import render
from testapp.forms import AddItemForm

# Create your views here.

def add_view(request):
	form = AddItemForm()
	if request.method == 'POST' :
		name = request.POST['name']
		quantity = request.POST['quantity']
		request.session[name] = quantity
		request.session.set_expiry(120)      # time in seconds
#		request.session.set_expiry(0)        # here session will depend on browser

	return render(request, 'testapp/additem.html', {'form':form})


def display_view(request):
	return render(request, 'testapp/displayitem.html')



def session_info_view(request) :
	session = request.session
	age = session.get_expiry_age()
	date = session.get_expiry_date()
	print('Exppiry Age : ', age)
	print('Expiry date : ', date)
	return render(request, 'testapp/additem.html')