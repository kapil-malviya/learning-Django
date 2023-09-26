from django.shortcuts import render

# Create your views here.

def show_details(request, my_id):        # my_id = 8
	if my_id == 1:
		student = {'id':my_id, 'name':'rajat'}
	if my_id == 8:
		student = {'id':my_id, 'name':'kapil'}
	if my_id == 28:
		student = {'id':my_id, 'name':'Anil'}
	if my_id == 888:
		student = {'id':my_id, 'name':'Ajay'}
	return render(request, 'testapp/show.html', student)



def home(request):
	return render(request, 'testapp/home.html')



def show(request, my_id, my_subid):
	if my_id == 1 and my_subid == 1001:
		student = {'id':my_id, 'name':'rajat', 'info':'Hyderabad'}
	if my_id == 8 and my_subid == 1008:
		student = {'id':my_id, 'name':'kapil', 'info':'dilli'}
	if my_id == 28 and my_subid == 1028:
		student = {'id':my_id, 'name':'Anil', 'info':'pune'}
	if my_id == 888 and my_subid == 1888:
		student = {'id':my_id, 'name':'Ajay', 'info':'Noida'}
	return render(request, 'testapp/show.html', student)
